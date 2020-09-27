from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:entry>/", views.entry_page, name="entry_page"),
    # path("wiki/search/<str:query>", views.search_entry, name="search_entry"),
]
