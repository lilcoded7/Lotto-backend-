from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *






router = DefaultRouter()

router.register("drawnumber", draw_number_view)
router.register("machine", machine_number_view)



app_name = "LOTTO"


urlpatterns = [
    path("", include(router.urls))
]