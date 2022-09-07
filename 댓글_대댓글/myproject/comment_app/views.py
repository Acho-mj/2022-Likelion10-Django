from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Comment, CommentReply
from .forms import PostForm, CommentForm, CommentReplyForm

# 메인 홈
def home(request):
    # posts = Post.objects.all() 
    posts = Post.objects.filter().order_by('-date')
    return render(request, 'home.html', {'posts': posts})


# 새 글 생성
def post_new(request):
    if request.method == 'POST' or request.method == "FILES":
        form = PostForm(request.POST, request.FILES)       
        if form.is_valid():
            unfinished = form.save(commit=False)
            unfinished.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form':form})

# 게시글 상세페이지
def post_detail(request, post_id):
    detail = get_object_or_404(Post, pk=post_id) 
    comment_form = CommentForm()
    comment_reply_form = CommentReplyForm()
    return render(request, 'post_detail.html', {'detail':detail, 'comment_form':comment_form, 'comment_reply_form':comment_reply_form})


# 댓글 
def comment_new(request, post_id):
    filled_form = CommentForm(request.POST)
    if filled_form.is_valid():
        finished_form = filled_form.save(commit=False)
        finished_form.post = get_object_or_404(Post, pk=post_id)
        finished_form.save()
    return redirect('post_detail', post_id)


# 대댓글
def commentreply(request, comment_id):
    form = CommentReplyForm(request.POST)
    if form.is_valid():
        finished = form.save(commit=False)
        finished.comment_reply = get_object_or_404(Comment, pk=comment_id)
        finished.save()
    return redirect('post_detail', post_id=finished.comment_reply.post.id)
