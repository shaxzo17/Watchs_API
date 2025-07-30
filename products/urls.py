from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import *

# #with mixins
# urlpatterns = [
#     path('' , WatchListCreateView.as_view()),
#     path('u/<int:pk>/' , WatchDetailView.as_view())
# ]


# #without mixins
# urlpatterns = [
#     path('', WatchListCreateView.as_view()),
#     path('u/<int:pk>/', WatchDelView.as_view())
# ]

#  #with ViewSet
router = DefaultRouter()
router.register(r'', WatchViewSet)

urlpatterns = router.urls