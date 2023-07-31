from django.urls import path
from .views import EventListCreateView, EventRetrieveUpdateDestroyView, LikeCreateDeleteView, EventDetailRegisterView, TagListView

urlpatterns = [
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(),
         name='event-retrieve-update-destroy'),
    path('events/<int:event_id>/like/',
         LikeCreateDeleteView.as_view(), name='event-like'),
    path('events/<int:pk>/register/', EventDetailRegisterView.as_view(),
         name='event-detail-register'),
    path('tags/', TagListView.as_view(), name='tag-list'),
]
