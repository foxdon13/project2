from django import forms
from .models import Post


class Post_Form(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"

    widgets = {
        "publish": forms.DateInput(attrs={"class": "form-control", "type": "date"})
    }
