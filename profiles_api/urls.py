from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(
    "hello-viewset", views.HelloViewSet, basename="hello-viewset"
)  # UserProfileViewSet
router.register("profile", views.UserProfileViewSet)
router.register("feed", views.UserFeedAPIViewSet)
urlpatterns = [
    path("hello-view/", views.HelloApiView.as_view()),
    path("login/", views.UserLoginApiView.as_view()),
    path("", include(router.urls)),
]
