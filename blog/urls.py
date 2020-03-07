from django.urls import path
from .views import BlogIndex, BlogDetail, BlogNew

urlpatterns = [
    path('', BlogIndex.as_view(), name='blog-index'),
    path('blog/<int:pk>', BlogDetail.as_view(), name='blog-detail'),
    path('blog/new', BlogNew.as_view(success_url="/"), name='blog-new')
]