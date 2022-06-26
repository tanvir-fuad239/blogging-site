from django.urls import path
from App_Login import views

app_name = 'App_Login'

urlpatterns = [
    path('signup/', views.sign_up, name='sign_up'),
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('profile/', views.display_profile, name='profile'),
    path('add-profile-pic/', views.add_profile_pic, name='add_profile_pic'),
    path('change-profile-pic/', views.change_profile_pic, name='change_profile_pic'),
    path('change-profile/', views.change_profile, name='change_profile'),
    path('password/', views.change_password, name='change_password'),
]
