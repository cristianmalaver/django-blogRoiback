from django.urls import path
from django.views.generic import TemplateView

# View
from users import views


urlpatterns = [

  

    # Management
    path(
        route = 'login/', 
        view = views.login_view, 
        name='login'
    ),
    path(
        route = 'logout/', 
        view = views.logout_view, 
        name='logout'
    ),
    path(
        route = 'signup/', 
        view = views.signup, 
        name ='signup'
    ),
    path(
        route = 'me/profile/', 
        view = views.update, 
        name='update'
    ),


    # Posts
    path(
        route='<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),
]