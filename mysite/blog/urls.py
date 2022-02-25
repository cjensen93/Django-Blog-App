from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('home/', views.index, name='index'),
    path('archive/', views.archive, name='archive'),
    path('<int:blog_id>/', views.entry, name='entry'),
    path('about/', views.about, name='about'),
    path('post/', views.post, name='post'),
    path('comment/', views.comment, name='comment'),
    path('techtips+css/', views.techWithCSS, name='techWithCSS'),
    path('techtips-css/', views.techWithoutCSS, name='techWithoutCSS'),
    path('plan', views.plan, name='plan')
]
