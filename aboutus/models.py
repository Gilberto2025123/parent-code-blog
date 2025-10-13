from django.db import models

# Create your models here.
class AboutUs(models.Model):
    title = models.CharField(max_length=200)
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class ContactForm(models.Model):
     name = models.CharField(max_length=100, unique=True)
     email = models.EmailField(max_length=200)
     subject = models.CharField(max_length=200)
     message = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     read = models.BooleanField(default=False)

     class Meta:
        ordering = ["-created_at"]

     
     def __str__(self):
        return self.name