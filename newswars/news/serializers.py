from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField
from .models import Channel, News


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class ChannelSerializer(ModelSerializer):
    news = NewsSerializer(many=True, read_only=True)

    class Meta:
        model = Channel
        fields = '__all__'