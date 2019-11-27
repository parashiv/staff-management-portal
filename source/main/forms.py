from django import forms
from .models import Posts, Leave, dependent
from django.contrib.auth.models import User
import datetime

class selectForm(forms.ModelForm):
"""! Creates a form for the dependent model, using the django ModelForm. Used to take the supervisor of a current staff as input and store the supervisor-staff mapping in the dependent model. The staff_name field is kept hidden. class Meta : An inner class to provide metadata to the ModelForm class. Provides an association between the ModelForm and the model dependent
    """
    staff_name = forms.HiddenInput()
    supervisor_name = forms.ModelChoiceField(queryset=User.objects.filter(is_superuser=True),required=True)
    class Meta:
	""" 
	"""        
	model = dependent
        fields = ('supervisor_name',)

class PostsForm(forms.ModelForm):
"""! Creates a form for the Posts model, using the django ModelForm. Used to take input the job post details posted by the supervisor and store them in the Post model. The author and post_published field is kept hidden. class Meta : An inner class to provide metadata to the ModelForm class. Provides an association between the ModelForm and the model Posts
    """
    job_title = forms.CharField(max_length=128, help_text="")
    job_date = forms.DateField(initial=datetime.date.today)
    job_location = forms.CharField(max_length=100)
    job_details = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 40}))
    post_published = forms.HiddenInput()
    author = forms.HiddenInput()
    class Meta:
        """ 
	"""        
	model = Posts
        fields = ('job_title','job_details','job_location','job_date')
        exclude = ['author']
        widgets = {
            'job_title': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'job_date': forms.DateField(
                
                ),
            'job_location': forms.TextInput(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'job_details': forms.Textarea(
                attrs={
                    'class': 'form-control'
                    }
                ),

            
            }


class LeaveForm(forms.ModelForm):
"""! Creates a form for the Leave model, using the django ModelForm. Used to take input the leave request details posted by the staff and store them in the Leave model. The author and approved field is kept hidden. Class Meta: An inner class to provide metadata to the ModelForm class. Provides an association between the ModelForm and the model Leave.
    """
    
    start_date = forms.DateField(initial=datetime.date.today)
    no_of_days = forms.IntegerField()
    reason = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 'cols': 40}))
    approved = forms.HiddenInput()
    author = forms.HiddenInput()
    class Meta:
	""" 
	"""        
	model = Leave
        fields = '__all__'
        exclude = ['author']
        widgets = {

            'start_date': forms.DateField(
                
                ),

            'no_of_days': forms.IntegerField(
                
                ),
            'reason': forms.Textarea(
                attrs={
                    'class': 'form-control'
                    }
                ),
            'approved': forms.HiddenInput()
            }



