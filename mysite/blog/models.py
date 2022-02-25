from django.db import models


class VisitorLog(models.Model):
    when = models.CharField(max_length=128, default=0)
    who = models.CharField(max_length=128)


class Blog(models.Model):
    title = models.CharField(max_length=128, default="title")
    author = models.CharField(max_length=128, default="author")
    content = models.TextField(max_length=10000, default="content")
    posted = models.CharField(max_length=128)
    commentNumber = models.CharField(max_length=128, default="0")


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    commenter = models.CharField(max_length=128, default="commenter")
    email = models.EmailField(max_length=128, default="email@email.com")
    content = models.TextField(max_length=10000, default="content")
    posted = models.CharField(max_length=128)
