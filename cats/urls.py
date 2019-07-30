from django.urls import path
from . import views

urlpatterns = [
    # Create a cat (Only accept POST)
    path('cats/create', views.createCat),
    # Fetch all the cats
    path('cats/show', views.catsList),
    # Fetch cat by its id. <int:cat_id> is the scope helps to pass id through web url, and it must be type or integor
    path('cats/<int:cat_id>/show', views.catById),
    # Remove cat by its id
    path('cats/<int:cat_id>/remove', views.catRemoveById),
]
