import os
from django.db import models
from django.conf import settings
from ckeditor_uploader.fields import RichTextUploadingField
import datetime

# Create your models here.
def imagePath():
    return os.path.join(settings.STATIC_URL, 'assets/images/blog')
    
class Post_Subjects(models.Model):
    subject = models.CharField(max_length=120) # max_length required
    image = models.ImageField(upload_to = 'subjects',null = True)
    status = models.BinaryField(default= 1)
    created_at = models.DateField(default=datetime.date.today) 
    # It will show the title in admin panel instead of objects(id)
    def __str__(self):
        return  self.subject

class Posts(models.Model):
    post_subject = models.ForeignKey(Post_Subjects, on_delete=models.CASCADE)
    title = models.CharField(max_length=120) # max_length required
    slug = models.SlugField(max_length=120) # max_length required
    summary = RichTextUploadingField(blank=False, null=False)
    image = models.ImageField(upload_to = 'blogs', blank = True)
    banner_image = models.ImageField(upload_to = 'banners', null= True)
    reference_url = models.URLField(max_length = 200, default='https://github.com/tauovir', blank = True)
    code = models.TextField(default='',blank=True)
    output = models.TextField(default='', blank=True)
    code_image = models.ImageField(upload_to = 'codes',default='', blank = True,null=True, help_text = 'Coding Image')
    output_image = models.ImageField(upload_to = 'outputs',default='',blank = True, null=True, help_text = 'Output image')
    comment_count = models.IntegerField(default=0)
    # It will show the title in admin panel instead of objects(id)
    def __str__(self):
        return  self.title

    class IsPublish(models.IntegerChoices):
        NOT_PUBLISH = 0
        PUBLISH = 1

    is_publish = models.IntegerField(choices=IsPublish.choices)
    publish_date = models.DateField(auto_now_add = False) 
    created_at = models.DateField(default=datetime.date.today) 
    updated_at = models.DateField(auto_now_add = True) 

    def get_absolute_url(self):
        return f"post_detail/{self.slug}"
    # @property
    # def days_since_creation(self):
    #     diff = timezone.now().date() - self.publish_date
    #     return diff.days 

class PostDetail(models.Model):
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    title = models.CharField(max_length=120) # max_length required
    summary = RichTextUploadingField(blank=False, null=False)
    code = models.TextField(default='',blank=True)
    output = models.TextField(default='', blank=True)
    image = models.ImageField(upload_to = 'blogs',blank = True,null=True,) # Defualt Image
    code_image = models.ImageField(upload_to = 'codes',default='', blank = True,null=True, help_text = 'Coding Image')
    output_image = models.ImageField(upload_to = 'outputs',default='',blank = True, null=True, help_text = 'Output image')
    
    class IsPublish(models.IntegerChoices):
        NOT_PUBLISH = 0
        PUBLISH = 1

    is_publish = models.IntegerField(choices=IsPublish.choices)
    publish_date = models.DateTimeField(auto_now_add = False) 
    created_at = models.DateField(default=datetime.date.today) 
    updated_at = models.DateField(auto_now_add = True) 
    """
    When you're using a ModelForm instance to create/edit a model, 
    the model's clean() method is guaranteed to be called. So, 
    if you want to strip whitespace from a field, you just add a clean() method to your model (no need to edit the ModelForm class):
    """
    def clean(self):
       if self.code:
           self.code = self.code.strip()
    # It will show the title in admin panel instead of objects(id)
    def __str__(self):
        return  self.title
    
   
class About(models.Model):
    brief_summary = RichTextUploadingField() 
    detail_summary = RichTextUploadingField() 
    skils = RichTextUploadingField(blank=False, null=False)
    blog_summary = RichTextUploadingField(blank=False, null=False)
    image = models.ImageField(upload_to = 'profiles')
    blog_image = models.ImageField(upload_to = 'profiles')
    created_at = models.DateField(default=datetime.date.today) 
    updated_at = models.DateField(auto_now_add = True) 
    
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=1)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250) # max_length required
    replied_on= models.IntegerField(default=0)
    created_at = models.DateField(default=datetime.date.today) 
    def __str__(self):
        return  self.comment

# class Contactus(models.Model):
#     name = models.CharField(max_length=100) # max_length required
#     email= models.EmailField(max_length = 150)
#     message= models.TextField()
#     created_at = models.DateField(default=datetime.datetime.now()) 
#     def __str__(self):
#         return  self.name

# =====================Creating Portfolio Model/Database ==============================

#==========================Master Tables===================================
class Languages(models.Model):
    name = models.CharField(max_length=20,null = True) # max_length required
    class status(models.IntegerChoices):
        active = 1
        not_active = 0
    is_other = models.IntegerField(default = 1, choices=status.choices)
    created_at = models.DateField(default=datetime.date.today) 
   
    def __str__(self):
        return  self.name

class Language_Proficiency(models.Model):
    name = models.CharField(max_length=20,null = True) # max_length required
    created_at = models.DateField(default=datetime.date.today) 

    def __str__(self):
        return  self.name

class Technology_Category(models.Model):
    name = models.CharField(max_length=120,null=False) # max_length required
    class status(models.IntegerChoices):
        active = 1
        not_active = 0
    status = models.IntegerField(default = 1, choices=status.choices)
    created_at = models.DateField(default=datetime.date.today) 
    
    def __str__(self):
        return  self.name

class Technologies(models.Model):
    category = models.ForeignKey(Technology_Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=120,null=False) # max_length required
    version = models.CharField(max_length=120, default = '', blank=True) # max_length required
    rate = models.SmallIntegerField(default = 70) # max_length required
    class isOther(models.IntegerChoices):
        yes = 1
        no = 0
    is_other = models.IntegerField(default = 0, choices=isOther.choices)

    def __str__(self):
        return  self.name
#==========================Master Tables end===================================

class Profile(models.Model):
    first_name = models.CharField(max_length=120,default='') # max_length required
    middle_name = models.CharField(max_length=120,default='') # max_length required
    last_name = models.CharField(max_length=120,default='') # max_length required
    profile_title = models.CharField(max_length=120,default='') # max_length required
    brief_summary = models.TextField(max_length=800,default='') # max_length required
    email = models.EmailField(max_length=50,default='') # max_length required
    mobile_number = models.CharField(max_length=15,default='') # max_length required
    profile_pic = models.ImageField(upload_to = 'profile')
    banner_image = models.ImageField(upload_to = 'profile')
    social_linkes = models.CharField(max_length=250,default='') # max_length required
    created_at = models.DateField(default=datetime.date.today) 
    updated_at = models.DateField(auto_now_add = True) 
    
    def __str__(self):
        return  self.first_name + " " + self.middle_name + " " + self.last_name

class Employment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    position = models.CharField(max_length=120,default='') # max_length required
    employer = models.CharField(max_length=120, null = False) # max_length required
    location = models.CharField(max_length=120, null = True) # max_length required
    summary = models.TextField(max_length=800,null=False) # max_length required
    start_date = models.DateField()
    end_date = models.DateField(blank = True,null = True)
    class isCurrent(models.IntegerChoices):
        yes = 1
        no = 0

    is_current_org = models.IntegerField(default = 0, choices=isCurrent.choices)
    created_at = models.DateField(default=datetime.date.today) 
    updated_at = models.DateField(auto_now_add = True) 
    def __str__(self):
        return  self.employer

class Projects(models.Model):
    employment = models.ForeignKey(Employment, on_delete=models.CASCADE)
    name = models.CharField(max_length=120,null=False) # max_length required
    description = models.TextField(max_length=800,null=False) # max_length required
    role_responsibility = models.TextField(max_length=300,null=False) # max_length required
    team_size = models.PositiveSmallIntegerField(default = 0)
    start_date = models.DateField()
    end_date = models.DateField(blank = True,null = True)
    technology = models.ManyToManyField(Technologies,db_table='blog_project_technology')
    created_at = models.DateField(default=datetime.date.today) 
   # technology = models.ManyToManyField(Technologies,through='Project_Technology')

    def __str__(self):
        return  self.name

# class Project_Technology(models.Model):
#     project = models.ForeignKey(Projects, on_delete=models.CASCADE)
#     technology = models.ForeignKey(Technologies, on_delete=models.CASCADE)
    

# class Project_Technology(models.Model):
#     project = models.ForeignKey(Projects, on_delete=models.CASCADE)
#     technology = models.ForeignKey(Technologies, on_delete=models.CASCADE)

class User_Language(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    language = models.ForeignKey(Languages, on_delete=models.CASCADE)
    language_profiency = models.ForeignKey(Language_Proficiency, on_delete=models.CASCADE)
    created_at = models.DateField(default=datetime.date.today) 

class Certificates(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=200,null = True) # max_length required
    short_name = models.CharField(max_length=100,null = True) # max_length required
    institute_short_name= models.CharField(max_length=50,null = True) # max_length required
    institute_full_name= models.CharField(max_length=100,null = True) # max_length required
    complition_date= models.DateField() # max_length required
    duration= models.CharField(max_length=100,null = True) # max_length required
    created_at = models.DateField(default=datetime.date.today) 
    def __str__(self):
        return  self.name

class Educations(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    course_short_name = models.CharField(max_length=100,null = True) # max_length required
    course_full_name = models.CharField(max_length=100,null = True) # max_length required
    institute_short_name= models.CharField(max_length=50,null = True) # max_length required
    institute_full_name= models.CharField(max_length=100,null = True) # max_length required
    university= models.CharField(max_length=100,null = True) # max_length required
    start_year= models.PositiveSmallIntegerField()
    end_year= models.PositiveSmallIntegerField()
    duration= models.CharField(max_length=100,null = True) # max_length required
    created_at = models.DateField(default=datetime.date.today) 
    class isSchool(models.IntegerChoices):
        yes = 1
        no = 0
    is_school = models.IntegerField(default = 0, choices=isSchool.choices)
    def __str__(self):
        return  self.course_full_name

class User_Interest(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    name = models.CharField(max_length=50,null = True) 
    created_at = models.DateField(default=datetime.date.today) 

# Contactus Form table
class Contactus(models.Model):
    name = models.CharField(max_length=100,null=False) # max_length required
    email = models.EmailField(max_length=120,null=False) # max_length required
    message = models.TextField(max_length=800,null=False) # max_length required
    created_at = models.DateField(default=datetime.date.today) 
    def __str__(self):
        return  self.name

# Signals is just like a triggers, After inserting comment,we are updating comment_count in post object
from django.db.models import signals
from django.dispatch import receiver

@receiver(signals.post_save, sender=Comment) 
def update_comment_count(sender, instance, created, **kwargs):
    print("================Comment signals Executed===============" )
    postObj = Posts.objects.get(id = instance.post.pk)
    postObj.comment_count += 1 
    postObj.save()