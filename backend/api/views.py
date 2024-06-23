from django.shortcuts import HttpResponse

from api.models import *

from api.serializers import *

from rest_framework import generics
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

def index(request):
  author = Author.objects.create(name="Bob", age=10)
  
  Book.objects.create(name="Book", price=10, author=author)
  
  return HttpResponse("Hello, world. You're at the api index.")
  
# -------------------------------------
# -----------------APIv1---------------
# -------------------------------------

# --------------Book api---------------
class BookList(generics.ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  
  filter_backends = [DjangoFilterBackend, filters.SearchFilter]
  filterset_fields = ['name']
  search_fields = ['name']
  

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer