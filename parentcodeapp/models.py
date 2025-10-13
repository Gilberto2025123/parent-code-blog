
from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="parentcodeapp_author"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="parentcodeapp_category"
    )
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    class Meta:
        ordering = ["-created_at"]


    def __str__(self):
        return f"{self.title} | written by {self.author}"

    


    


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="parentcodeapp_comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="parentcodeapp_commenter"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_at"]


    def __str__(self):
        return f"Comment: {self.content} by {self.author}"


class ContactForm(models.Model):
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.name
    


class Bookmarks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parentcodeapp_bookmarks")
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="parentcodeapp_bookmarks")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Blog saved by {self.user}"

class JobPost(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    description = models.TextField()
    apply_link = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="parentcodeapp_jobs")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ["-created_at"]  

    def __str__(self):
        return f"{self.title} at {self.company}"
   
class MyProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)

    # profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    

    def __str__(self):
        return f"{self.user.username}'s profile"