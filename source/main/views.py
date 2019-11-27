from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Posts, Leave, dependent
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.views.generic import CreateView
from .forms import PostsForm, LeaveForm, selectForm
# Create your views here.

def homepage(request):
"""! Defines what action to perform when the view 'homepage' is called from urls. Sends the template index.html as HTTPResponse (for the homepage)
	
    @param request The HTTPRequest object
    @return HTTPResponse object conatining the template for homepage
    """
	return render(request=request,
				  template_name="main/index.html",	
					)

def posts(request):
"""! Defines what action to perform when the view 'posts' is called from urls. Sends the template posts.html as HTTPResponse, along with all the Posts objects as dict to be used as the template’s context for rendering.	
    @param request The HTTPRequest object
    @return HTTPResponse object containing the template and context containing the Posts objects
    """
	return render(request=request,
				  template_name="main/posts.html",
				  context={"posts": Posts.objects.all}	
					)

def leave_requests(request):
"""! Defines what action to perform when the view 'leave_requests' is called from urls. Used to view the leave requests made by the staffs of the current supervisor. Sends the template leave_requests.html as HTTPResponse, along with those leave requests made only by the staffs of the current supervisor as the template’s context for rendering.	
    @param request The HTTPRequest object
    @return HTTPResponse object containing the template and context containing the leaves objects
    """
	super_name=request.user.username
	staffs=dependent.objects.filter(supervisor_name=super_name).values('staff_name')
	leaves = Leave.objects.filter(author__in=staffs)
	return render(request=request,
				  template_name="main/leave_requests.html",
				  context={"posts": leaves}  
					)

def select_supervisor(request):
"""! Defines what action to perform when the view 'select_supervisor' is called from urls. Saves the data collected from selectForminto the model dependent, along with setting the satff_name of the model dependent to the current user's username. Sends the template select_super.html as HTTPResponse, along with the django form for getting the supervisor of the cuurent user(a dropdown select option), as the template’s context for rendering.	
    @param request The HTTPRequest object
    @return HTTPResponse object containing the template and context containing the form selectForm to get the supervisor of current user.
    """	
	# A HTTP POST?
	if request.method == 'POST':
		form = selectForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
			post = form.save(commit=False)
			post.staff_name = request.user.username
			post.save()
			# Save the new category to the database.
			#form.save(commit=True)
			# Now call the index() view.
			# The user will be shown the homepage.
			return redirect("main:posts")
		else:
			# The supplied form contained errors - just print them to the terminal.
			print (form.errors)
	else:
		# If the request was not a POST, display the form to enter details.
		form = selectForm()

	# Bad form (or form details), no form supplied...
	# Render the form with error messages (if any).
	
	return render(request=request,
				  template_name="main/select_super.html",	
				  context={'form': form})


def create_posts(request):
"""! Defines what action to perform when the view 'create_posts' is called from urls. Used to create new posts for job by the supervisors, for the staffs. Sends the template create_post.html as HTTPResponse, along with the django form for getting the post details posted by the current user, as the template’s context for rendering.	
    @param request The HTTPRequest object
    @return HTTPResponse object containing the template and context containing the django form PostsForm 
    """	
	# A HTTP POST?
	if request.method == 'POST':
		form = PostsForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user.username
			post.save()
			# Save the new category to the database.
			#form.save(commit=True)
			# Now call the index() view.
			# The user will be shown the homepage.
			return redirect("main:posts")
		else:
			# The supplied form contained errors - just print them to the terminal.
			print (form.errors)
	else:
		# If the request was not a POST, display the form to enter details.
		form = PostsForm()

	# Bad form (or form details), no form supplied...
	# Render the form with error messages (if any).
	return render(request=request,
				  template_name='main/create_post.html', 
				  context={'form': form}
				  )


def leave(request):
"""! Defines what action to perform when the view 'leave' is called from urls. Used to create new leave requests by the staffs. Sends the template apply_leave.html as HTTPResponse, along with the django form for getting the leave request details posted by the current user, as the template’s context for rendering.	
    @param request The HTTPRequest object
    @return HTTPResponse object containing the template and context containing the django form LeaveForm 
    """	
	# A HTTP POST?
	if request.method == 'POST':
		form = LeaveForm(request.POST)

		# Have we been provided with a valid form?
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user.username
			post.save()

			# Now call the index() view.
			# The user will be shown the homepage.
			return redirect("main:posts")
		else:
			# The supplied form contained errors - just print them to the terminal.
			print (form.errors)
	else:
		# If the request was not a POST, display the form to enter details.
		form = LeaveForm()

	# Bad form (or form details), no form supplied...
	# Render the form with error messages (if any).
	return render(request=request,
				  template_name='main/apply_leave.html', 
				  context={'form': form}
				  )    
def register(request):
"""! Defines what action to perform when the view 'register' is called from urls. Used to redirect to a page having choices for registering as Supervisor or Staff.. Sends the template choices.html as HTTPResponse, along with the django form for getting the post details posted by the current user, as the template’s context for rendering.	
    @param request The HTTPRequest object
    @return HTTPResponse object containing the template for choices  
    """
	return render(request=request,
				  template_name="main/choices.html",	
					)


def register_staff(request):
"""! Defines what action to perform when the view 'register_staff' is called from urls. Used to create new staff account and save it to the User model. Sends the template register.html as HTTPResponse, along with the django form for getting the leave request details posted by the current user and 'super' as false , as the template’s context for rendering.	
    @param request The HTTPRequest object
    @return HTTPResponse object containing the template and context containing the django form UserCreationForm and the value of super as false 
    """
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)			
			profile.is_superuser = False
			profile.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"Staff Account Created: {username}" )
			login(request, profile)
			return redirect("main:select_supervisor")
		else:
			for msg in	form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

	form = UserCreationForm
	return render(request=request,
				  template_name="main/register.html",
				  context={"form": form,"super": False}	
					)

def register_supervisor(request):
"""! Defines what action to perform when the view 'register_supervisor' is called from urls. Used to create new supervisor account and save it to the User model. Sends the template register.html as HTTPResponse, along with the django form for getting the leave request details posted by the current user and 'super' as true , as the template’s context for rendering.	
    @param request The HTTPRequest object
    @return HTTPResponse object containing the template and context containing the django form UserCreationForm and the value of super as true 
    """
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			profile = form.save(commit=False)			
			profile.is_superuser = True
			profile.save()
			username = form.cleaned_data.get('username')
			messages.success(request, f"Supervisor Account Created: {username}" )
			login(request, profile)
			return redirect("main:posts")
		else:
			for msg in	form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

	form = UserCreationForm
	return render(request=request,
				  template_name="main/register.html",
				  context={"form": form,"super": True}	
					)	

def logout_request(request):
"""! Defines what action to perform when the view 'logout_request' is called from urls. Used to log out the current user.	
    @param request The HTTPRequest object
    @return Redirects to the homepage view
    """
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("main:homepage")

def login_request(request):
"""! Defines what action to perform when the view 'login_request' is called from urls. Used to log in an user. Displays appropriate error message, if any. Sends the template login.html as HTTPResponse, along with the django form for log in , as the template’s context for rendering.	
    @param request The HTTPRequest object
    @return HTTPResponse object containing the template and context containing the django form AuthenticationForm 
    """
	if request.method == 'POST':
		form = AuthenticationForm(request=request, data=request.POST)
		if form.is_valid():
			
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.success(request, f"You are now logged in as {username}")
				return redirect('/posts')
			else:
				messages.error(request, "Invalid username or password.")
		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request = request,
					template_name = "main/login.html",
					context={"form":form})    	
