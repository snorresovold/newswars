from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Channel, News

class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'

class ChannelSerializer(ModelSerializer):
    news = SerializerMethodField()

    def get_news(self, obj):  # allows us to filter what news we get
        news = list(reversed(obj.news.all()))[:24] # get 24 nested news (reversed)
        return NewsSerializer(news, many=True).data 

    class Meta:
        model = Channel
        fields = '__all__'
