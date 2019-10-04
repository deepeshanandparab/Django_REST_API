from django.urls import path
from .views import ArticleView

app_name = "article_api"

urlpatterns = [
    path('', ArticleView.as_view()),
    path('<int:pk>', ArticleView.as_view())
]