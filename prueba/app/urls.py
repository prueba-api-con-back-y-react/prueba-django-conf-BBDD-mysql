from django.urls import path
from .views import *

urlpatterns = [
    path('persons/',PersonView.as_view(), name="v1"),
    path('persons/<int:id>',PersonView.as_view(), name="v2"),
]
