from django.shortcuts import render, get_object_or_404

from django.views import generic
from .models import Post, Category

# Create your views here.
class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = 'parentcodeapp/index.html'
    paginate_by = 6

    
def post_detail(request, slug):
    """
    Display an individual :model:`parentcodeapp.Post`.

    **Context**

    ``post``
        An instance of :model:`parentcodeapp.Post`.

    **Template:**

    :template:`parentcodeapp/post_detail.html`
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.parentcodeapp_comments.all().order_by("-created_at")
    comment_count = post.parentcodeapp_comments.filter(is_approved=True).count()

    return render(
        request,
        "parentcodeapp/post_detail.html",
        {"post": post, 
         "comments": comments, 
         "comment_count": comment_count},
    )

