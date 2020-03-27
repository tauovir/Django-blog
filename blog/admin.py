from django.contrib import admin

# Register your models here.
from blog.models import Posts,PostDetail,About

class PostsAdmin(admin.ModelAdmin):
    pass

class PostDetailAdmin(admin.ModelAdmin):
    pass

admin.site.register(Posts)
admin.site.register(PostDetail)
admin.site.register(About)




