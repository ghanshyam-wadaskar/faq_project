# Create your views here.
from rest_framework import generics
from .models import FAQ
from .serializers import FAQSerializer

from django.http import HttpResponse


def home(request):
    return HttpResponse(
        "<h1>Welcome to the FAQ API</h1>"
        "<p>Use <code>/api/faqs/</code> to access the FAQ API.</p>"
    )


class FAQListCreateView(generics.ListCreateAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer


class FAQDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
