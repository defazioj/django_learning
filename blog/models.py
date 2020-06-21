from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    # we're not putting parenthesis after timezone.now b/c we don't
    # want to execute the function at that point,
    # we just want to pass in the actual function as the default value
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # 2nd arg above just tells django that we want users' posts to be
    # deleted as well if their profile is deleted
    # corey also mentions that this is a way way street and that deleting a post
    # does not delete the user


# once we save this file and run makemigrations, we can see this
# Class reflected in the migrations/0001_initial_.py file
