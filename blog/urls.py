from blog import views
from django.urls import path

urlpatterns = [
    path('post_list/', views.post, name='post-list'),
    path("author_post/<int:pk>", views.author_post, name="author-posts"),
    path('post/<int:pk>', views.post_detail, name="post-detail")
]
