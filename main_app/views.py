from django.shortcuts import render, redirect
from django.contrib import messages ##added for validations

from .models import *


def index(request):
	return redirect('/shows_list')

def shows(request):
    context = {"shows": Shows.objects.all()}
    return render(request, 'shows_list.html', context)

def add_show(request):
    return render(request, 'add_new_show.html')

def show_added(request):
    print (request.POST)
    errors = Shows.objects.basic_validator(request.POST)
    print(errors)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        
        return redirect("/shows/new")

    else:
        added_show = Shows.objects.create(
            title = request.POST["title"],
            network = request.POST["network"],
            release_date = request.POST["release_date"],
            desc = request.POST["desc"]
        )
        messages.success(request, "Show successfully added")
    print(request.POST)
    return redirect(f'/shows/{added_show.id}')

def edit_show(request, show_id):

    context = {"shows": Shows.objects.get(id=show_id)}
    return render(request, 'edit_shows.html', context)

def submit_edit(request, show_id):
    print (request.POST)
    errors = Shows.objects.basic_validator(request.POST)
    print(errors)
    if len(errors):
        for key, value in errors.items():
            messages.error(request, value)

        return redirect(f'/shows/{edited_show.id}')

    else:
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
    return redirect(f'/shows/{edited_show.id}/edit')

def show_listing(request, show_id):
    context = {"shows": Shows.objects.get(id=show_id)}
    return render(request, 'show_descriptions.html', context)

def delete_show(request, show_id):
    Shows.objects.get(id=show_id).delete()
    return redirect('/shows_list')

def update(request, show_id):
    errors = Shows.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect(f'/shows/{edited_show.id}') 
##I need 2 of these for edited and also for adding a new one don't I..
## if that's the case then the method would be the same just a different def name and diff redirect link i believve
