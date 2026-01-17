from . import views
from django.urls import path


urlpatterns = [
    path('', views.PostList.as_view(), name='home'),
    path('my-profile/', views.my_profile, name='my_profile'),
    path('job-postings/', views.job_postings, name='job_postings'),
    path('my-bookmarks/', views.my_bookmarks, name='my_bookmarks'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]
