from django.contrib import admin
from django.urls import path, include
from Qapp import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', views.home, name='home'),
    path('postcreate', views.postcreate, name='postcreate'),
    path('detail/<int:post_id>', views.detail, name='detail'),
    path('new_comment/<int:post_id>', views.new_comment, name='new_comment'),

]

# media 파일에 접근할 수 있는 url도 추가해주어야 함    
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



