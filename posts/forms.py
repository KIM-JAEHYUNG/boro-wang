from django import forms
from .models import Post
from django.utils.translation import gettext_lazy as _

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'price', 'content', 'location', 'user', 'shows', 'areas']
        labels = {
            'title': "제목",
            'image': "이미지",
            'price': "가격",
            'location': "위치",
            'content': "내용",
            'shows': "공연종류",
            'areas': "지역",
        }
        widgets = {
            'user': forms.HiddenInput(),
        }