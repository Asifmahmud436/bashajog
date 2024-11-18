from rest_framework.viewsets import ModelViewSet
from .serializers import BuildingSerializer,UnitSerializer
from .models import Building,Unit
from rest_framework import filters
from .pagination import BuildingPagination,UnitPagination

# building viewset
class BuildingViewSet(ModelViewSet):
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer
    pagination_class = BuildingPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['owner__user__username']

# unit viewset
class UnitViewSet(ModelViewSet):
    queryset = Unit.objects.all()
    serializer_class = UnitSerializer
    pagination_class = UnitPagination
    
    def get_queryset(self):
        queryset = Unit.objects.all()
        is_occupied = self.request.query_params.get('is_occupied','').lower()
        room = self.request.query_params.get('rooms')

        if is_occupied in ['true','false']:
            queryset = queryset.filter(is_occupied=is_occupied == 'true')
        if room:
            queryset = queryset.filter(room=room)

        return queryset
