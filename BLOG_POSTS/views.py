from django.core.checks import messages
from django.shortcuts import redirect, render
from .models import Post
from django.shortcuts import get_object_or_404
from .forms import Post_Form

# Create your views here.


def post_list(request):
    posts = Post.objects.all()
    return render(request, "BLOG_POSTS/POST_LIST.html", {"posts": posts})


def post_detail(request, slug, year, month, day):
    post = get_object_or_404(
        Post,
        publish__year=year,
        publish__month=month,
        publish__day=day,
        slug=slug,
        status="published",
    )

    return render(request, "BLOG_POSTS/POST_DETAIL.html", {"post": post})


def post_create(request):
    # form = BookForm(request.POST or None)
    if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("post_list")

    else:
        form = Post_Form()

    return render(request, "BLOG_POSTS/POST_FORM.html", {"form": form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = Post_Form(request.POST, instance=post)

        if form.is_valid():
            form.save()
            return redirect(
                "post_detail",
                post.slug,
                post.publish.year,
                post.publish.month,
                post.publish.day,
            )
    else:
        form = Post_Form(instance=post)

    return render(request, "BLOG_POSTS/POST_FORM.html", {"form": form})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        post.delete()
        return redirect("post_list")

    return render(request, "BLOG_POSTS/POST_DELETE.html", {"post": post})
