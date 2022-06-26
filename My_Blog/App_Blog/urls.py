from django.urls import path
from App_Blog import views

app_name = 'App_Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('write/', views.CreateBlog.as_view(), name='write_blog'),
    path('blog-details/<pk>/', views.blog_details, name='blog_details'),
    path('liked/<pk>/', views.liked, name='liked'),
    path('unliked/<pk>/', views.unliked, name='unliked'),
    path('my-blogs', views.my_blogs, name='my_blogs'),
    path('edit-blog/<pk>/', views.edit_blog, name='edit_blog'),
    path('delete-blog/<pk>/', views.DeleteBlog.as_view(), name='delete_blog'),
    path('view-profile/<str:user>/', views.view_profile, name='view_profile'),
]
