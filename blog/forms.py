from django import forms
from .models import Post

class Postform(forms.ModelForm):
    model = Post
    fields = ('title', 'text', )