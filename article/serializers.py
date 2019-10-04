from rest_framework import serializers
from .models import Article

class ArticleSerializers(serializers.Serializer):
    title = serializers.CharField(max_length=200)
    description = serializers.CharField()
    body = serializers.CharField()
    author_id = serializers.IntegerField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.title = validate_data.get('title', instance.title)
        instance.description = validate_data.get('description', instance.description)
        instance.body = validate_data.get('body', instance.body)
        instance.author_id = validate_data.get('author_id', instance.author_id)

        instance.save()
        return instance