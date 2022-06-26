from django import forms
from App_Blog.models import Comment,Blog

class CommentForm(forms.ModelForm):
    class Meta:

        model = Comment
        fields = ('comment',)

class EditBlogForm(forms.ModelForm):
    class Meta:

        model = Blog
        fields = ('blog_title', 'blog_content', 'blog_image')
