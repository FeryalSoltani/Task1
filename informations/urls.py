from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'data', views.DataCRUDViewSet, base_name='data')

urlpatterns = [
    url(r'', views.DataList.as_view()),
    url(r'<int:pk>/', views.DataDetail.as_view()),
] + router.urls
