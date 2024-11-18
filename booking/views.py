from django.shortcuts import render
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet
from .models import Booking
from .serializers import BookingSerializer
from django.db.models import Q
from rest_framework import filters


class BookingPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'page_size'
    max_page_size = 100

class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    pagination_class = BookingPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['unit__building__owner__user__username']
    ordering_fields = ['rent']


