from django.urls import path
from . import views



urlpatterns = [
    path('', views.home, name='blog-home'),
    path('', views.feed_view, name='blog-feed')
]

urlpatterns += [
    path('accounts/register/', views.register_view, name='blog-accounts-register'),
    path('accounts/login/', views.login_view, name='blog-accounts-login'),
    path('accounts/logout/', views.logout_view, name='blog-accounts-logout'),
    path('accounts/user/<int:id>/', views.user_profile_view, name='blog-accounts-profile'),
    path('accounts/user/<int:id>/follow/', views.user_follow_view, name='blog-accounts-profile-follow'),
    path('accounts/user/<int:id>/unfollow/', views.user_follow_view, name='blog-accounts-profile-unfollow')
]

urlpatterns += [
    path('post/<int:id>/', views.post_detail, name='blog-post-detail'),
    path('post/<int:id>/comment/', views.new_comment, name='blog-post-comment'),
    path('post/new/', views.new_post, name='blog-post-new')
]
