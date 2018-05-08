from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .models import Bookmark

from .forms import BookmarkForm


def index(request):
    if request.method == 'POST':
        target_id = request.POST['id']
        target_bookmark = Bookmark.objects.filter(pk=target_id)
        target_bookmark.delete()
    bookmark_list = Bookmark.objects.all()
    return render(request, 'bookmarks/index.html', {'bookmark_list': bookmark_list})


def add_bookmark(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            Bookmark(form['url'], form['name'], form['notes']).save()
            return HttpResponseRedirect('/bookmarks/')

    else:
        form = BookmarkForm()
    return render(request, 'bookmarks/bform.html', {'form': form})
