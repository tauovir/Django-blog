# from django.db.models import signals
# from django.dispatch import receiver
# from blog.models import Comment

# # post_save method
# @receiver(signals.post_save, sender=Comment) 
# def update_comment_count(sender, instance, created, **kwargs):
#     print("================Executed signals===============" )
#     # print(instance.post)