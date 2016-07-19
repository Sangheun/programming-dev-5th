from django import forms

from .models import Pokemon, Trainer, CatchInfo

class PokemonForm(forms.ModelForm):
    class Meta:
        model = Pokemon
        fields = '__all__'

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = '__all__'

class CatchInfoForm(forms.ModelForm):
    class Meta:
        model = CatchInfo
        fields = '__all__'

