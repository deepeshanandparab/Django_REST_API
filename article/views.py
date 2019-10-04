from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Article
from .serializers import ArticleSerializers


class ArticleView(APIView):
    def get(self, request, pk=None):
        if pk:
            articles = get_object_or_404(Article.objects.all(), pk=pk)
            serializer = ArticleSerializers(articles)
            return Response({'articles:': serializer.data})
        articles = Article.objects.all()
        serializer = ArticleSerializers(articles, many=True)
        return Response({'articles': serializer.data})

    def post(self, request, pk=None):
        article = request.data.get('article')

        serializer = ArticleSerializers(data=article)
        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({'Success':'Article \'{}\' created Successfully'.format(article_saved.title)})

    def put(self, request, pk):
        saved_article = get_object_or_404(Article.objects.all(), pk=pk)
        data = request.data.get('article')
        serializer = ArticleSerializers(data)

        if serializer.is_valid(raise_exception=True):
            article_saved = serializer.save()
        return Response({'Success':'Article \'{}\' updated Successfully'.format(article_saved.title)})

    def delete(self, request, pk):
        article = get_object_or_404(Article.objects.all(), pk=pk)
        article.delete()
        return Response({'message':'Article {} has been deleted'.format(pk)}, status=204)