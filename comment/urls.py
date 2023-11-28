from django.urls import path

from comment import views

urlpatterns = [
    path('create/<int:info_pk>/', views.CommentCreateView.as_view(), name='comment-create'),
]