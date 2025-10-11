from django.shortcuts import render, get_object_or_404

from django.views import generic
from .models import Post, Category, Comment


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
    
        return render(
            request,
            "parentcodeapp/post_detail.html",
            {"post": post},
        )

