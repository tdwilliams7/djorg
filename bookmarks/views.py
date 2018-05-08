from django.shortcuts import render

# Create your views here.
from django.http import HttpResponseRedirect
from .models import Bookmark

from .forms import BookmarkForm


def index(request):
    bookmark_list = Bookmark.objects.all()
    return render(request, 'bookmarks/index.html', {'bookmark_list': bookmark_list})


def add_bookmark(request):
    if request.method == 'POST':
        form = BookmarkForm(request.POST)
        if form.is_valid():
            form = form.cleaned_data
            print(form)
            new_bookmark = Bookmark(form['url'], form['name'], form['notes'])
            new_bookmark.save()
            return HttpResponseRedirect('/bookmarks/')

    else:
        form = BookmarkForm()
    return render(request, 'bookmarks/bform.html', {'form': form})
