from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Blog(models.Model):

    author = models.ForeignKey(User, related_name='blog_author', on_delete=models.CASCADE, verbose_name='Author')
    blog_title = models.CharField(max_length=500, verbose_name='Put a title')
    slug = models.SlugField(unique=True, verbose_name='Slug')
    blog_content = models.TextField(verbose_name='Blog content')
    blog_image = models.ImageField(upload_to='blog_images', blank=True)
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:

        ordering = ('-publish_date',)

    def __str__(self):

        return self.blog_title

class Comment(models.Model):

    blog = models.ForeignKey(Blog, related_name='blog_comment', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='blog_user', on_delete=models.CASCADE)
    comment = models.TextField(verbose_name='Comment')
    comment_date = models.DateTimeField(auto_now_add=True)


    class Meta:

        ordering = ('-comment_date',)

    def __str__(self):

        return self.comment


class Likes(models.Model):

    blog = models.ForeignKey(Blog, related_name='liked_blog', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='liked_user', on_delete=models.CASCADE)

    def __str__(self):

        return self.user + " likes " + self.blog
    