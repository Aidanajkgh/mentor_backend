from rest_framework.views import APIView
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView
from rest_framework.response import Response

from .models import Announcement
from .serializers import (
    AnnouncementSerializers,
    AnnouncementListSerializers, 
    AnnouncementCreateSerializers,
    AnnouncementRetrieveSerializers,
)

class MentorView(APIView):
    def get(self, request, *args, **kwargs):
        ads = Announcement.objects.all()
        ads_json = AnnouncementListSerializers(ads, many=True)
        return Response(ads_json.data, status=200)
    
    def post(self, request):
        data = request.data
        serializer = AnnouncementCreateSerializers(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        # else:
        #     return Response(serializer.errors, status=400)
        

class AnnouncementRetrieveView(RetrieveAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializers


class AnnouncementUpdateView(UpdateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializers


class AnnouncementDeleteView(DestroyAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializers


class AnnouncementCreateView(CreateAPIView):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializers
