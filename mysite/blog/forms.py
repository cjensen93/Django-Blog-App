from django import forms


class BlogForm(forms.Form):
    title = forms.CharField(label="title", max_length=128)
    author = forms.CharField(label="author", max_length=128)
    content = forms.CharField(label="content", max_length=10000)


class CommentForm(forms.Form):
    blog = forms.CharField(label="blog", max_length=128)
    commenter = forms.CharField(label="commenter", max_length=128)
    email = forms.CharField(label="email", max_length=128)
    content = forms.CharField(label="content", max_length=10000)
