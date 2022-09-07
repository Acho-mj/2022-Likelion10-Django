from django.contrib import admin
from django.urls import path
from comment_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    
    path('post_new', views.post_new, name='post_new'),
    path('post_detail/<int:post_id>', views.post_detail, name='post_detail'),
    path('comment_new/<int:post_id>', views.comment_new, name='comment_new'),
    path('commentreply/<int:comment_id>', views.commentreply, name='commentreply'),
    
]
