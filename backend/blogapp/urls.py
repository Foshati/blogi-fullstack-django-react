from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .import views

router = DefaultRouter()
router.register("blogs", views.PostModelViewSet)

urlpatterns = [
     path("", include(router.urls))
]

# get_recent_blogs = http://127.0.0.1:8008/blogs/recent
# sepecific_blog = http://127.0.0.1:8008/blogs/:slug