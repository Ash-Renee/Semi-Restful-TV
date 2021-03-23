from django.shortcuts import render, redirect
from .models import Shows


def index(request):
	return redirect('/shows_list')

def shows(request):
    context = {"shows": Shows.objects.all()}
    return render(request, 'shows_list.html', context)

def add_show(request):
    return render(request, 'add_new_show.html')


def show_added(request):
    added_show = Shows.objects.create(
        title = request.POST["title"],
        network = request.POST["network"],
        release_date = request.POST["release_date"],
        desc = request.POST["desc"]
    )
    print(request.POST)
    return redirect(f'/shows/{added_show.id}')

def edit_show(request, show_id):
    context = {"shows": Shows.objects.get(id=show_id)}
    return render(request, 'edit_shows.html', context)

def submit_edit(request, show_id):
    edited_show = Shows.objects.get(id=show_id)
    if request.POST['title']:
        edited_show.title = request.POST['title']

    if request.POST['network']:
        edited_show.network = request.POST['network']

    if request.POST['release_date']:
        edited_show.release_date = request.POST['release_date']

    if request.POST['desc']:
        edited_show.desc = request.POST['desc']

    edited_show.save()
    print(request.POST)
    return redirect(f'/shows/{edited_show.id}')

def show_listing(request, show_id):
    context = {"shows": Shows.objects.get(id=show_id)}
    return render(request, 'show_descriptions.html', context)

def delete_show(request, show_id):
    Shows.objects.get(id=show_id).delete()
    return redirect('/shows_list')

