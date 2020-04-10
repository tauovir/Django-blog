import os
from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
def imagePath():
    return os.path.join(settings.STATIC_URL, 'assets/images/blog')
    
class Posts(models.Model):
    title = models.CharField(max_length=120) # max_length required
    slug = models.SlugField(max_length=120) # max_length required
    summary = RichTextUploadingField(blank=False, null=False)
    image = models.ImageField(upload_to = 'blog_image')

    banner_image = models.ImageField(upload_to = 'banner_image', blank = True)
    reference_url = models.URLField(max_length = 200, default='https://github.com/tauovir')
    # It will show the title in admin panel instead of objects(id)
    def __str__(self):
        return  self.title

    class IsPublish(models.IntegerChoices):
        NOT_PUBLISH = 0
        PUBLISH = 1

    is_publish = models.IntegerField(choices=IsPublish.choices)
    publish_date = models.DateTimeField(auto_now_add = False) 
    created_at = models.DateTimeField() 
    updated_at = models.DateTimeField(auto_now_add = True) 


class PostDetail(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    title = models.CharField(max_length=120) # max_length required
    summary = RichTextUploadingField(blank=False, null=False)
    code = RichTextUploadingField(blank=False, null=False)
    image = models.ImageField(upload_to = 'blog_image')
    class IsPublish(models.IntegerChoices):
        NOT_PUBLISH = 0
        PUBLISH = 1

    is_publish = models.IntegerField(choices=IsPublish.choices)
    publish_date = models.DateTimeField(auto_now_add = False) 
    created_at = models.DateTimeField() 
    updated_at = models.DateTimeField(auto_now_add = True) 
    # It will show the title in admin panel instead of objects(id)
    def __str__(self):
        return  self.title
   
   
class About(models.Model):
    brief_summary = RichTextUploadingField() 
    detail_summary = RichTextUploadingField() 
    skils = RichTextUploadingField(blank=False, null=False)
    blog_summary = RichTextUploadingField(blank=False, null=False)
    image = models.ImageField(upload_to = 'profile')
    blog_image = models.ImageField(upload_to = 'profile')
    created_at = models.DateField() 
    updated_at = models.DateField(auto_now_add = True) 
    # It will show the title in admin panel instead of objects(id)