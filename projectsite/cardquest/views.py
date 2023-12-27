from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Trainer , Collection

from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from cardquest.models import Trainer
from django.urls import reverse_lazy
from cardquest.models import Collection
# views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import PokemonCard

def pokemon_cards(request):
    pokemon_cards = PokemonCard.objects.all()
    return render(request, 'pokemon_cards.html', {'pokemon_cards': pokemon_cards})

class add_pokemon_card(CreateView):
    model = PokemonCard
    template_name = 'pokemon_add.html'  # Change this to your actual template name
    fields = ['name', 'rarity', 'hp', 'card_type', 'attack', 'description', 'weakness', 'card_number', 'release_date', 'evolution_stage', 'abilities', 'image_url']
    success_url = reverse_lazy('pokemon-card-list')

class EditPokemonCardView(UpdateView):
    model = PokemonCard
    template_name = 'pokemon_edit.html'
    fields = ['name', 'rarity', 'hp', 'card_type', 'attack', 'description', 'weakness', 'card_number', 'release_date', 'evolution_stage', 'abilities', 'image_url']
    success_url = reverse_lazy('pokemon-card-list')


def delete_pokemon_card(request, card_id):
    card = get_object_or_404(PokemonCard, id=card_id)
    
    # Add logic to handle deleting a Pokemon card
    # Assuming you have some logic to delete the card, for example:
    card.delete()
    
    # Redirect to the success URL after deletion
    return redirect('pokemon-card-list')

class CollectionAddView(CreateView):
    model = Collection
    template_name = 'collection_add.html'
    fields = ['trainer', 'card', 'quantity']
    success_url = reverse_lazy('collection-list')

class CollectionEditView(UpdateView):
    model = Collection
    template_name = 'collection_edit.html'
    fields = ['trainer', 'card', 'quantity']
    success_url = reverse_lazy('collection-list')

class CollectionDeleteView(DeleteView):
    model = Collection
    template_name = 'collection_del.html'
    success_url = reverse_lazy('collection-list')

class TrainerAddView(CreateView):
    model = Trainer
    template_name = 'trainer_add.html'
    fields = ['name', 'birthdate', 'location', 'email']
    success_url = reverse_lazy('trainer-list')  

class TrainerEditView(UpdateView):
    model = Trainer
    template_name = 'trainer_edit.html'
    fields = ['name', 'birthdate', 'location', 'email']
    success_url = reverse_lazy('trainer-list')

class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'trainer_del.html'
    success_url = reverse_lazy('trainer-list')


class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "base.html"
    def get_context_data(self, **kwargs):
       context = super().get_context_data(**kwargs)
       return context

class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by =50

class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemon_cards'
    template_name = 'pokemon-cards.html'
    paginate_by = 8

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collections'
    template_name = "collections.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Include the related Trainer and PokemonCard in the context
        context['collections'] = Collection.objects.select_related('trainer', 'card').all()
        return context

# In the view
def my_view(request):
    pokemon_cards = PokemonCard.objects.all()

    # Print image URLs for debugging
    for card in pokemon_cards:
        print(f"{card.name}: {card.image_url}")

    return render(request, 'pokemon-cards.html', {'pokemon_cards': pokemon_cards})

