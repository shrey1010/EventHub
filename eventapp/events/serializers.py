from rest_framework import serializers
from .models import Event, Like,Tag
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = ['user', 'registered_users']

    def update(self, instance, validated_data):
        tags_data = validated_data.pop('tags', [])
        for field, value in validated_data.items():
            setattr(instance, field, value)
        instance.save()

        # Update tags
        instance.tags.clear()
        for tag_data in tags_data:
            tag, _ = Tag.objects.get_or_create(name=tag_data['name'])
            instance.tags.add(tag)

        return instance

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        # Add custom data to the token response, if needed
        # For example, you can include user data in the token response
        data['username'] = self.user.username
        return data
