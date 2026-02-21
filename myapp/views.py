from django.shortcuts import render, redirect
from myapp.models import Bookmark
from myapp.forms import BookmarkForm

def display(request):
    b = Bookmark.objects.all()
    d = {'data': b}
    return render(request, 'myapp/index.html', d)

def insert(request):
    f = BookmarkForm()
    if request.method == 'POST':
        f = BookmarkForm(request.POST)
        if f.is_valid():
            f.save(commit=True)
            return redirect('/')
    d = {'form': f}
    return render(request, 'myapp/insert.html', d)

def update(request, id):
    b = Bookmark.objects.get(id=id)
    if request.method == 'POST':
        f = BookmarkForm(request.POST, instance=b)
        if f.is_valid():
            f.save(commit=True)
            return redirect('/')
    ctx = {'bm': b}
    return render(request, 'myapp/update.html', ctx)

def delete(request, id):
    b = Bookmark.objects.get(id=id)
    b.delete()
    return redirect('/')