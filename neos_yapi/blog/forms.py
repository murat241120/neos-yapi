from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):
    body = forms.CharField(label ='Konu', widget=forms.Textarea(attrs={'rows': 4,'placeholder': 'Konu hakkında birkaç cümle yaz...'}))
    title = forms.CharField(label='Başlık', widget=forms.TextInput(attrs={'placeholder': 'Bir konu başlığı oluştur...'}))
    class Meta:
        model = Post
        fields = ('title', 'body')

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'body')


class CommentForm(forms.ModelForm):
    content = forms.CharField(
    label='', widget=forms.TextInput(attrs={'placeholder': 'Bir yorum ekle....'}))

    class Meta:
        model = Comment
        fields = ('content',)

class CommentUpdateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)