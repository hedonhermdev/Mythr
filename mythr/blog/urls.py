from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:id>/', views.post_detail, name='blog-post-detail'),
    path('post/<int:id>/comment/', views.new_comment, name='blog-post-comment'),
    path('post/new/', views.new_post, name='blog-post-new')
]

urlpatterns += [
    path('accounts/register/', views.register_view, name='blog-accounts-register'),
    path('accounts/login/', views.login_view, name='blog-accounts-login'),
    path('accounts/logout/', views.logout_view, name='blog-accounts-logout')
]