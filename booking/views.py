from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Booking
from .serializers import BookingSerializer
from django.db.models import Q


class BookingPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100
class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = BookingPagination

    def get_queryset(self):
        queryset = Booking.objects.all()
        owner_username = self.request.query_params.get('owner_username')
        if owner_username:
            queryset = queryset.filter(unit__building__owner__user__username__icontains=owner_username).distinct()
        return queryset

