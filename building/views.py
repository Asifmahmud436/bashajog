from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from .serializers import BuildingSerializer,UnitSerializer
from .models import Building,Unit

# building views
class BuildingPagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 500

class BuildingViewSet(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    pagination_class = BuildingPagination

    def get_queryset(self):
        queryset = Building.objects.all()
        owner_username = self.request.query_params.get('owner_username')
        if owner_username:
            queryset = queryset.filter(owner__user__username__icontains=owner_username).distinct()
        return queryset
    
    
# unit views
class UnitPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 500
    
class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    pagination_class = UnitPagination

    def get_queryset(self):
        queryset = Unit.objects.all()
        is_occupied = self.request.query_params.get('is_occupied')
        room = self.request.query_params.get('rooms')

        if is_occupied:
            queryset = queryset.filter(is_occupied=is_occupied)
        if room:
            queryset = queryset.filter(room=room)

        return queryset
