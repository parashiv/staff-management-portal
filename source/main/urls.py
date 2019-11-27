"""
Used to perform certain views against certain url requests
Is a mapping between URL path expressions to Python functions (the views).
"""
from django.urls import path
from . import views

#name of the app
app_name= "main"

##contain the url patterns and their respective views
urlpatterns = [
	path('', views.homepage, name="homepage"),
	path('posts/', views.posts, name="posts"),
	path('register/',views.register, name="register"),
	path('staff/',views.register_staff, name="register_staff"),
	path('supervisor/',views.register_supervisor, name="register_supervisor"),
	path("logout/", views.logout_request, name="logout"),
	path("login/", views.login_request, name="login"),
	path("add_post/", views.create_posts, name="create_post"),
	path("apply_leave/", views.leave, name="apply_leave"),
	path("leave_requests/",views.leave_requests, name='leave_requests'),
	path("select_supervisor/", views.select_supervisor, name='select_supervisor'),
]
