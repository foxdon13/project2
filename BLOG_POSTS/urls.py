from django.urls import path
from .views import post_delete, post_detail, post_edit, post_list, post_create

urlpatterns = [
    path("posts/", post_list, name="post_list"),
    path(
        "post/<slug:slug>/<int:year>/<int:month>/<int:day>/",
        post_detail,
        name="post_detail",
    ),
    path("post/create/", post_create, name="post_create"),
    path("post/edit/<int:pk>", post_edit, name="post_edit"),
    path("post/delete/<int:pk>", post_delete, name="post_delete"),
]
