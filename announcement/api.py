#from rest_framework.views import APIView
#from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView
#from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser ,IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter

from users.permissions import IsOwnerOrReadOnly
from .pagination import AnnounccementPagination

from .models import Announcement, Subcategory, Category
from .serializers import (
    AnnouncementDetailSerializers,
#    AnnouncementListSerializers, 
#    AnnouncementCreateSerializers,
#    AnnouncementRetrieveSerializers,
    AnnouncementSerializers,
    SubcategorySerializer,
    CategorySerializer,
)


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class SubcategoryViewSet(ModelViewSet):
    queryset = Subcategory.objects.all()
    permission_classes = [IsAdminUser]
    serializer_class = SubcategorySerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    permission_classes = [IsOwnerOrReadOnly]
    pagination_class = AnnounccementPagination
    serializer_class = AnnouncementSerializers
    filter_backends = [SearchFilter]
    search_fields = ['title', 'description']

    def get_serializer_class(self):
        if self.action == 'list' or self.action == 'retrieve':
            return AnnouncementDetailSerializers
        else:
            return AnnouncementSerializers

# class MentorView(APIView):
#     def get(self, request, *args, **kwargs):
#         ads = Announcement.objects.all()
#         ads_json = AnnouncementListSerializers(ads, many=True)
#         return Response(ads_json.data, status=200)
    
#     def post(self, request):
#         data = request.data
#         serializer = AnnouncementCreateSerializers(data=data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             return Response(serializer.data, status=201)
        # else:
        #     return Response(serializer.errors, status=400)
        

# class AnnouncementRetrieveView(RetrieveAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializers

# class AnnouncementUpdateView(UpdateAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializers

# class AnnouncementDeleteView(DestroyAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializers

# class AnnouncementCreateView(CreateAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializers


# class AnnouncementRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializers


