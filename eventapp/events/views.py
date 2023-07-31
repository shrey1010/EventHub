from rest_framework import generics, status, filters
from rest_framework.response import Response
from .models import Event, Like,Tag
from .serializers import EventSerializer, LikeSerializer,CustomTokenObtainPairSerializer,TagSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['date', 'time']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]


class LikeCreateDeleteView(generics.CreateAPIView, generics.DestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def get_event_object(self):
        event_id = self.kwargs.get('event_id')
        return generics.get_object_or_404(Event, id=event_id)

    def post(self, request, *args, **kwargs):
        event = self.get_event_object()
        like, created = Like.objects.get_or_create(
            event=event, user=request.user)
        return Response({'created': created}, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        event = self.get_event_object()
        Like.objects.filter(event=event, user=request.user).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventDetailRegisterView(generics.RetrieveAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        event = self.get_object()
        event.registered_users.add(request.user)
        return Response({'message': 'You have registered for the event.'}, status=status.HTTP_200_OK)


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
