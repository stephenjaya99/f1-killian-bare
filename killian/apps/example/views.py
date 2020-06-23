from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView

from .serializers import ExampleSerializer
from killian.libs.loading import get_model

Example = get_model('example', 'Example')


class ExampleListCreateView(ListCreateAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer


class ExampleDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
    lookup_field = 'id'
