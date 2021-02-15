from django.urls import path
from .views import article_list, article_by_id, article_title_update

urlpatterns = [
    path('article/', article_list),
    path('detail/<int:pk>', article_by_id),
    path('title/<int:pk>', article_title_update)
]