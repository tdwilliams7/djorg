from rest_framework import serializers, viewsets
from .models import Note, User
from django.conf import settings
from django.conf.urls import url
from rest_framework.authtoken import views as drf_views
from django.http import HttpResponse

# Serializers define the API Respresentation


class NoteSerializer(serializers.HyperlinkedModelSerializer):
    """serializer to define the API Respresentation for Notes"""
    class Meta:
        model = Note
        fields = ('title', 'content', 'id')

    def create(self, validated_data):
        """Override create to associate current user with new note"""
        user = self.context['request'].user
        note = Note.objects.create(user=user, **validated_data)
        return note


class UserSerializer(serializers.ModelSerializer):
    class meta:
        model = User
        fields = ('username')


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        if pk == 'i':
            return HttpResponse(UserSerializer(request.user,
                                               context={'request': request}).data)
        return super(UserViewSet, self).retrieve(request, pk)


class NoteViewSet(viewsets.ModelViewSet):
    """ViewSet to define the view behaivor for notes"""
    serializer_class = NoteSerializer
    #queryset = Note.objects.filter(api_enabled=True)
    queryset = Note.objects.none()

    def get_queryset(self):
        user = self.request.user
        if user.is_anonymous:
            return Note.objects.none()
        else:
            return Note.objects.filter(user=user)
