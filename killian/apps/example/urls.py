from django.urls import re_path

from .views import ExampleDetailView
from .views import ExampleListCreateView


urlpatterns = [
    re_path(r'^examples$', ExampleListCreateView.as_view(), name='example-list'),
    re_path(r'^examples/(?P<id>[^/]+)$',
            ExampleDetailView.as_view(), name='example-detail'),
]
