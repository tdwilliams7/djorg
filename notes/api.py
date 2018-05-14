from rest_framework import serializers, viewsets
from .models import Note

# Serializers define the API Respresentation


class NoteSerializer(serializers.HyperLinkedModelSerializer):
    """serializer to define the API Respresentation for Notes"""
    class Meta:
        model = Note
        fields = ('title', 'content')


class NoteViewSet(viewsets.ModelViewSet):
    """ViewSet to define the view behaivor for notes"""
    serializer_class = NoteSerializer
    #queryset = Note.objects.filter(api_enabled=True)
    queryset = Note.objects.all()
