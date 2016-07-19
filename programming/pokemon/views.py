from django.shortcuts import render, get_object_or_404, redirect

from .models import Person, Pokemon, Place, Show
from .forms import PokemonForm


def index(request):
    pokemon = Pokemon.objects.all()
    person = Person.objects.all()
    place = Place.objects.all()

    return render(request, 'pokemon/index.html', {
    'person':person,
    'pokemon':pokemon,
    'place':place,
        })

def pokemon(request):
    return render(request, 'pokemon/pokemon.html', {
        })

def place(request):
    return render(request, 'pokemon/place.html', {

        })

def person(request):
    return render(request, 'pokemon/person.html', {

        })

def catch(request):
    pass

def show(request):
    pass


def pokemon_name_new(request):
    if request.method == "POST":
        form = PokemonForm(request.POST)
        if form.is_valid():
            form = PokemonForm(request.POST)
            form.save()
            return redirect('pokemon:pokemon')
    else:
        form = PokemonForm()

    return render(request, 'pokemon/pokemon.html', {
        'form':form
        })


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/detail.html', {
#         'question': question
#     })

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, 'polls/results.html', {
#         'question':question
#         })