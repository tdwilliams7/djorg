from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Bookmark


def index(request):
    bookmark_list = Bookmark.objects.all()
    output = ', '.join([b.name for b in bookmark_list])
    return render(request, 'bookmarks/index.html', {'bookmark_list': bookmark_list})
