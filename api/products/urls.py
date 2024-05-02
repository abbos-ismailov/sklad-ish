from django.urls import path
from .views import (
    XomashyoGetApiView
)


urlpatterns = [
    path("material/", XomashyoGetApiView.as_view()),
]