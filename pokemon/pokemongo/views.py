from django.shortcuts import render, redirect

from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm, CatchInfoForm


def pokemon_list(request):
    pokemons = Pokemon.objects.all()
    trainers = Trainer.objects.all()
    return render(request, 'pokemongo/pokemon_list.html', {
        'pokemons':pokemons,
        'trainers':trainers,
        })

def add_pokemon(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            pokemon = form.save()
            return redirect('pokemongo:pokemon_list')
    else:
        form = PokemonForm()
    return render(request, 'pokemongo/add_pokemon.html', {'form':form})

def add_trainer(request):
    if request.method == "POST":
        form = TrainerForm(request.POST)
        if form.is_valid():
            trainer = Trainer.objects.create(name=form.cleaned_data['name'])

            return redirect('pokemongo:pokemon_list')
    else:
        form = PokemonForm()
    return render(request, 'pokemongo/add_trainer.html', {'form':form})

