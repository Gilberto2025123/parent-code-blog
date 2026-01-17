from . import views
from django.urls import path

# URL patterns for blog-related pages
# Note: These URLs are prefixed with 'blog/' from the main urls.py
urlpatterns = [
    # Main blog page - shows list of all posts
    path('', views.PostList.as_view(), name='blog_home'),
    
    # User profile pages (placeholders for now)
    path('my-profile/', views.my_profile, name='my_profile'),
    path('job-postings/', views.job_postings, name='job_postings'),
    path('my-bookmarks/', views.my_bookmarks, name='my_bookmarks'),
    
    # Comment management - these must come before post_detail
    # Otherwise the slug pattern would catch them first
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    
    # Individual post page - shows full post and comments
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
