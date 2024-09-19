from django.urls import path, include
from . import views
from .api.routers import router as api_router

urlpatterns = [
    path('', view=views.home),
    path('api/', include(api_router.urls))
]
