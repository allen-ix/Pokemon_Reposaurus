from django.shortcuts import render
from django.views.generic.list import ListView
from cardquest.models import PokemonCard, Trainer, Collection

class CollectionList(ListView):
    model = Collection
    context_object_name = 'collection'
    template_name = 'collection.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(CollectionList, self).get_queryset(*args, **kwargs)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class PokemonCardList(ListView):
    model = PokemonCard
    context_object_name = 'pokemon_cards'
    template_name = 'pokemon_cards.html'
    paginate_by = 5

    def get_queryset(self, *args, **kwargs):
        qs = super(PokemonCardList, self).get_queryset(*args, **kwargs)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class HomePageView(ListView):
    model = PokemonCard
    context_object_name = 'home'
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class TrainerList(ListView):
    model = Trainer
    context_object_name = 'trainer'
    template_name = 'trainers.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(TrainerList, self).get_queryset(*args, **kwargs)
        return qs


# trainers/views.py


from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Trainer
from projectsite.forms import TrainerForm, PokemonCardForm  # Import the form you use for editing
from projectsite.forms import TrainerAddForm, PokemonAddForm
from django.views import View

class TrainerAddView(View):
    template_name = 'add_trainer.html'

    def get(self, request):
        form = TrainerAddForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = TrainerAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trainer-list')  # Redirect to the trainer list after adding a new trainer
        return render(request, self.template_name, {'form': form})

class TrainerUpdateView(UpdateView):
    model = Trainer
    form_class = TrainerForm
    template_name = 'edit_trainer.html'
    success_url = reverse_lazy('trainer-list')  # Redirect to the trainer list after editing

    def form_valid(self, form):
        # Additional logic if needed before saving the form
        return super().form_valid(form)


class TrainerDeleteView(DeleteView):
    model = Trainer
    template_name = 'delete_trainer.html'
    success_url = reverse_lazy('trainer-list')  # Redirect to the trainer list after deletion

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    


class PokemonUpdateView(UpdateView):
    model = PokemonCard
    form_class = PokemonCardForm
    template_name = 'edit_pokemon.html'
    success_url = reverse_lazy('pokemon-card-list')  # Redirect to the trainer list after editing

    def form_valid(self, form):
        # Additional logic if needed before saving the form
        return super().form_valid(form)


class PokemonDeleteView(DeleteView):
    model = PokemonCard
    template_name = 'delete_pokemon.html'
    success_url = reverse_lazy('pokemon-card-list')  # Redirect to the trainer list after deletion

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
    
class PokemonAddView(View):
    template_name = 'add_pokemon.html'

    def get(self, request):
        form = PokemonAddForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PokemonAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pokemon-card-list') 
        return render(request, self.template_name, {'form': form})
