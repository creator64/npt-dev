from django.urls import path
from django.conf.urls.static import static

from django.conf import settings

from . import views


urlpatterns = [
path("", views.collection, name="npt"),
path("bekijkId=<int:id>", views.view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)