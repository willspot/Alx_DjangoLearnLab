from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Tag, Comment
from taggit.forms import TagWidget
from taggit.managers import TaggableManager


class PostForm(forms.ModelForm):
    # Using TagWidget() directly
    tags = forms.CharField(
        required=False,
        widget=TagWidget()  # Use TagWidget to create the widget for tags
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # Exclude author field since it's set automatically

    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) < 5:
            raise forms.ValidationError("Title must be at least 5 characters long.")
        return title
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Write your comment here...'})
        }

class PostForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']