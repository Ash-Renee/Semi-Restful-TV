from django.urls import path
from . import views

urlpatterns = [

    path('', views.index),
    path('shows_list', views.shows),
    path('shows/new', views.add_show),
    path('shows/create', views.show_added),
    path('shows/<int:show_id>/edit', views.edit_show),
    path('shows/<int:show_id>/submit_edit', views.submit_edit),
    path('shows/<int:show_id>', views.show_listing),
    path('shows/<int:show_id>/destroy', views.delete_show),
]
