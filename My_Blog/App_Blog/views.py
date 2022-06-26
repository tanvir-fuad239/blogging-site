from django.http import HttpResponse
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.models import User
from App_Login.models import UserProfile
from App_Blog.models import Blog,Comment,Likes
from App_Blog.forms import CommentForm,EditBlogForm
from django.views.generic import TemplateView,ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse,reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

import uuid

# Create your views here.


class BlogList(ListView):

    context_object_name = 'blogs'
    model = Blog
    template_name = 'App_Blog/blog_list.html'


class CreateBlog(LoginRequiredMixin,CreateView):
    
   
    model = Blog
    fields = ('blog_title', 'blog_content', 'blog_image')
    template_name = 'App_Blog/create_blog.html'

    def form_valid(self, form):

        form_obj = form.save(commit=False)

        form_obj.author = self.request.user
        title = form_obj.blog_title
        form_obj.slug = title.replace(" ", "-") + "-" + str(uuid.uuid4())
        form_obj.save()
        return HttpResponseRedirect(reverse('App_Blog:blog_list'))

def blog_details(request, pk):

    if request.user.is_authenticated:

        blog = Blog.objects.get(pk=pk) 

        already_liked = Likes.objects.filter(blog=blog, user=request.user)

        if not already_liked:

            liked = True

        else:

            liked = False


        comment = CommentForm()

        if request.method == 'POST':

            comment = CommentForm(data=request.POST)

            if comment.is_valid():

                form_obj = comment.save(commit=False)
                form_obj.blog = blog
                form_obj.user = request.user
                form_obj.save()
                return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'pk' : pk}))


        dict = {'blog' : blog, 'comment' : comment, 'liked' : liked}
        return render(request, 'App_Blog/blog_details.html', context=dict)


    else:
        return HttpResponseRedirect(reverse('App_Login:login'))
    
 
@login_required
def liked(request, pk):

    blog = Blog.objects.get(pk=pk)
    user = request.user

    already_liked = Likes.objects.filter(blog=blog, user=user)

    if not already_liked:

        liked_post = Likes(blog=blog,user=user)
        liked_post.save()

        return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'pk' : pk}))


@login_required
def unliked(request, pk):

    blog = Blog.objects.get(pk=pk)
    user = request.user

    already_liked = Likes.objects.filter(blog=blog, user=user)

    already_liked.delete()

    return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'pk' : pk}))


@login_required
def my_blogs(request):

    dict = {}
    return render(request, 'App_Blog/my_blogs.html', context=dict)

@login_required
def edit_blog(request, pk):

    blog = Blog.objects.get(pk=pk)

    form = EditBlogForm(instance=blog)

    if request.method == 'POST':
        form = EditBlogForm(request.POST, request.FILES, instance=blog)

        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse('App_Blog:blog_details', kwargs={'pk' : pk}))


    dict = {'form' : form}
    return render(request, 'App_Blog/edit_blog.html', context=dict)

class DeleteBlog(LoginRequiredMixin, DeleteView):

    model = Blog
    template_name = 'App_Blog/delete_blog.html'
    success_url = reverse_lazy('App_Blog:blog_list')


 
def view_profile(request, user):

    if request.user.is_authenticated:


        current_user = request.user    

        if current_user.username == user:

            return HttpResponseRedirect(reverse('App_Login:profile'))

        else:

            user_obj = User.objects.get(username=user)
            first_name = user_obj.first_name
            last_name = user_obj.last_name
            username = user_obj.username
            email = user_obj.email

             
            
            dict = {'first_name' : first_name, 'last_name' : last_name, 'username' : username, 'email' : email}
            return render(request, 'App_Blog/public_profile.html', context=dict)
    

    else:

        return HttpResponseRedirect(reverse('App_Login:login'))

