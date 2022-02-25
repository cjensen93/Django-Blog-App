from django.shortcuts import render, get_object_or_404
from .models import VisitorLog, Blog, Comment
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from .forms import BlogForm, CommentForm


def index(request):
    visitor = VisitorLog()
    dateString = datetime.now()
    dateString = dateString.strftime("%Y-%m-%d %H:%M:%S")
    visitor.when = dateString
    visitor.who = request.META['REMOTE_ADDR']
    visitor.save()
    visits = list(VisitorLog.objects.all())
    visitsLen = len(visits)
    if len(visits) > 10:
        visits = visits[-10:]

    blogPost = list(Blog.objects.all())[-3:]
    blogPost.reverse()
    context = {'visits': visits,
               'visitsLen': visitsLen,
               'blogPost': blogPost}

    return render(request, 'blog/index.html', context)


@csrf_exempt
def post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        newPost = Blog()
        dateString = datetime.now()
        dateString = dateString.strftime("%Y-%m-%d %H:%M:%S")
        if form.is_valid():
            title = form.cleaned_data['title']
            author = form.cleaned_data['author']
            content = form.cleaned_data['content']
            newPost.title = title
            newPost.author = author
            newPost.content = content
            newPost.posted = dateString
            newPost.commentNumber = "0"
        newPost.save()

        visitor = VisitorLog()
        dateString = datetime.now()
        dateString = dateString.strftime("%Y-%m-%d %H:%M:%S")
        visitor.when = dateString
        visitor.who = request.META['REMOTE_ADDR']
        visitor.save()
        visits = list(VisitorLog.objects.all())
        visitsLen = len(visits)
        if len(visits) > 10:
            visits = visits[-10:]

        blogPost = list(Blog.objects.all())[-3:]
        blogPost.reverse()
        context = {'visits': visits,
                   'visitsLen': visitsLen,
                   'blogPost': blogPost}

        return render(request, 'blog/index.html', context)


@csrf_exempt
def comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        for i in form:
            print(i)
        newComment = Comment()
        dateString = datetime.now()
        dateString = dateString.strftime("%Y-%m-%d %H:%M:%S")
        blog_id = None
        if form.is_valid():
            commenter = form.cleaned_data['commenter']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']
            blog_id = int(form.cleaned_data['blog'])
            newComment.blog = Blog.objects.get(pk=blog_id)
            print(newComment.blog)
            print(blog_id)
            newComment.commenter = commenter
            newComment.email = email
            newComment.content = content
            newComment.posted = dateString
        newComment.save()

    blogEntry = get_object_or_404(Blog, pk=blog_id)
    commentAdder = int(blogEntry.commentNumber)
    commentAdder += 1
    blogEntry.commentNumber = str(commentAdder)
    blogEntry.save()
    commentEntry = list(Comment.objects.filter(blog=blog_id))
    commentEntry.reverse()
    context = {'blogEntry': blogEntry,
               'commentEntry': commentEntry}

    return render(request, 'blog/entry.html', context)


def about(request):
    visitor = VisitorLog()
    dateString = datetime.now()
    dateString = dateString.strftime("%Y-%m-%d %H:%M:%S")
    visitor.when = dateString
    visitor.who = request.META['REMOTE_ADDR']
    visitor.save()
    visits = list(VisitorLog.objects.all())
    visitsLen = len(visits)
    if len(visits) > 10:
        visits = visits[-10:]
    context = {'visits': visits,
               'visitsLen': visitsLen}

    return render(request, 'blog/about.html', context)


def techWithCSS(request):
    visitor = VisitorLog()
    dateString = datetime.now()
    dateString = dateString.strftime("%Y-%m-%d %H:%M:%S")
    visitor.when = dateString
    visitor.who = request.META['REMOTE_ADDR']
    visitor.save()
    visits = list(VisitorLog.objects.all())
    visitsLen = len(visits)
    if len(visits) > 10:
        visits = visits[-10:]
    context = {'visits': visits,
               'visitsLen': visitsLen}

    return render(request, 'blog/techtips+css.html', context)


def techWithoutCSS(request):
    visitor = VisitorLog()
    dateString = datetime.now()
    dateString = dateString.strftime("%Y-%m-%d %H:%M:%S")
    visitor.when = dateString
    visitor.who = request.META['REMOTE_ADDR']
    visitor.save()
    visits = list(VisitorLog.objects.all())
    visitsLen = len(visits)
    if len(visits) > 10:
        visits = visits[-10:]
    context = {'visits': visits,
               'visitsLen': visitsLen}

    return render(request, 'blog/techtips-css.html', context)


def archive(request):
    visitor = VisitorLog()
    dateString = datetime.now()
    dateString = dateString.strftime("%Y-%m-%d %H:%M:%S")
    visitor.when = dateString
    visitor.who = request.META['REMOTE_ADDR']
    visitor.save()
    visits = list(VisitorLog.objects.all())
    visitsLen = len(visits)
    if len(visits) > 10:
        visits = visits[-10:]

    blogPost = list(Blog.objects.all())
    blogPost.reverse()
    context = {'visits': visits,
               'visitsLen': visitsLen,
               'blogPost': blogPost}

    return render(request, 'blog/archive.html', context)


def entry(request, blog_id):
    blogEntry = get_object_or_404(Blog, pk=blog_id)
    commentEntry = list(Comment.objects.filter(blog=blog_id))
    commentEntry.reverse()
    visitor = VisitorLog()
    dateString = datetime.now()
    dateString = dateString.strftime("%Y-%m-%d %H:%M:%S")
    visitor.when = dateString
    visitor.who = request.META['REMOTE_ADDR']
    visitor.save()
    visits = list(VisitorLog.objects.all())
    visitsLen = len(visits)
    if len(visits) > 10:
        visits = visits[-10:]

    context = {'blogEntry': blogEntry,
               'commentEntry': commentEntry,
               'visits': visits,
               'visitsLen': visitsLen}

    return render(request, 'blog/entry.html', context)


def plan(request):
    visitor = VisitorLog()
    dateString = datetime.now()
    dateString = dateString.strftime("%Y-%m-%d %H:%M:%S")
    visitor.when = dateString
    visitor.who = request.META['REMOTE_ADDR']
    visitor.save()
    visits = list(VisitorLog.objects.all())
    visitsLen = len(visits)
    if len(visits) > 10:
        visits = visits[-10:]

    context = {'visits': visits,
               'visitsLen': visitsLen,}
    return render(request, 'blog/plan.html', context)
