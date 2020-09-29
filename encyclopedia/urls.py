from django.urls import path


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>/", views.entry_page, name="entry_page"),
    path("wiki/<str:entry>/edit", views.edit_entry, name="edit_entry"),
    path("new/", views.add_entry, name="add_entry"),
    path("random/", views.random_entry, name="random_entry"),
]
