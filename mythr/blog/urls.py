from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:id>/', views.post_detail, name='blog-post-detail'),
    path('post/<int:id>/comment/', views.new_comment, name='blog-post-comment'),
    path('post/new/', views.NewPostView.as_view(), name='blog-new-post')
]
