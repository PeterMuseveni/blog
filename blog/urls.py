from django.urls import path, include
from .views import Index,DetailArticleView,LikeArticle,DeleteArticleView,Featured

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('tinymce/', include('tinymce.urls')), 
    path('<int:pk>/', DetailArticleView.as_view(), name='detail_article'),
    path('<int:pk>/like', LikeArticle.as_view(), name='like_article'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article'),
    path('featured/', Featured.as_view(), name='featured'),
    path('<int:pk>/delete', DeleteArticleView.as_view(), name='delete_article')




   
]