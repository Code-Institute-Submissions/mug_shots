from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery, name='gallery'),
    path('new_review/', views.new_review, name='new_review'),
    path('delete_review/<int:review_id>/',
         views.delete_review, name='delete_review'),
    path('edit_review/<int:review_id>/',
         views.edit_review, name='edit_review'),
]
