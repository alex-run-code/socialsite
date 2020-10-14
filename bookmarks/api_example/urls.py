from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('images/', views.ImageList.as_view()),
    path('images/<slug>', views.ImageList.as_view()),
    path('images/<int:pk>/', views.ImageDetail.as_view()),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

# urlpatterns = format_suffix_patterns(urlpatterns)