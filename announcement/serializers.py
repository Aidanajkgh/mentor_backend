from rest_framework import serializers

from .models import Announcement


class AnnouncementListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['id', 'title', 'description']

class AnnouncementCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = ['title', 'description']

class AnnouncementRetrieveSerializers(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'

class AnnouncementSerializers(serializers.ModelSerializer):
    class Meta:
        model = Announcement
        fields = '__all__'