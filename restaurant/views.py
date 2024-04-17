from django.shortcuts import render
from rest_framework import generics
from .models import Menu
from .models import Booking
from .serializers import MenuSerializer
from .serializers import BookingSerializer
from rest_framework import viewsets

# Create your views here.
def index(request):
  return render(request, 'index.html', {})

class MenuItemView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
