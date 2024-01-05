import statistics

from core import settings
from . import views
from django.urls import path
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='home'),
    path('posts', views.PostList.as_view(), name='posts'),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)