"""
URL configuration for projectsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

from django.urls import path
from cardquest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.HomePageView.as_view(),name='home'),
]

from cardquest.views import HomePageView, TrainerList, PokemonCardList ,CollectionList, EditPokemonCardView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HomePageView.as_view(), name='home'),
    path('trainer_list/', TrainerList.as_view(), name='trainer-list'),
    path('trainer_add', views.TrainerAddView.as_view(), name='trainer-add'),
    path('trainer_edit/<int:pk>/', views.TrainerEditView.as_view(), name='trainer-edit'),
    path('trainer_del/<int:pk>/', views.TrainerDeleteView.as_view(), name='trainer-delete'),
    path('pokemon-card-list/', PokemonCardList.as_view(), name='pokemon-card-list'),
    path('collections/', CollectionList.as_view(), name='collection-list'),
    path('collections/add/', views.CollectionAddView.as_view(), name='collection-add'),
    path('collections/edit/<int:pk>/', views.CollectionEditView.as_view(), name='collection-edit'),
    path('collections/delete/<int:pk>/', views.CollectionDeleteView.as_view(), name='collection-delete'),
    path('pokemon-cards/', views.pokemon_cards, name='pokemon_cards'),
    path('add-pokemon-card/', views.add_pokemon_card.as_view(), name='add_pokemon_card'),
    path('edit-pokemon-card/<int:pk>/', EditPokemonCardView.as_view(), name='edit_pokemon_card'),
    path('delete-pokemon-card/<int:card_id>/', views.delete_pokemon_card, name='delete_pokemon_card'),
]