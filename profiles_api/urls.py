from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api.views import HelloViewSet, HelloApiView, UserProfileViewSet


router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profiles', UserProfileViewSet)


urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls)),
]
