from django import forms
from .models import Post, Comment, CommentReply

class PostForm(forms.ModelForm):
    body = forms.CharField(label='', widget=forms.Textarea(attrs={
        'class': 'post-new-content',
        'rows': 5,
        'cols': 50,
        'placeholder': '140자 까지 등록 가능합니다.', }))

    class Meta:
        model = Post
        fields = ['title', 'body']
        
        
        
class CommentForm(forms.ModelForm):
    comment = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 5,
        'cols': 50,
        'placeholder': '댓글을 적어 주세요.', }))

    class Meta:
        model = Comment
        fields = ['comment']
        
class CommentReplyForm(forms.ModelForm):
    content = forms.CharField(label='', widget=forms.Textarea(attrs={
        'rows': 5,
        'cols': 50,
        'placeholder': '대댓글을 입력해주세요.', }))

    class Meta:
        model = CommentReply
        fields = ['content']