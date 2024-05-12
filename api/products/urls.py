from django.urls import path
from .views import (
    MaterialGetApiView
)


urlpatterns = [
    path("material/", MaterialGetApiView.as_view()),
]