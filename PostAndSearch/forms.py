from django import forms
from django.forms import ModelForm
from .models import Game, GameType, Platform, Series, Language, Company, Target, Room


# class GameIndexForm(forms.Form):
#     game_option = forms.ModelChoiceField(queryset=Game.english_name)

class GameSelectForm(ModelForm):
    class Meta:
        model = Game
        fields = ['chinese_name', 'english_name', 'japanese_name']


class RoomCreate(ModelForm):
    class Meta:
        model = Room
        exclude = ('game', 'guest_id', 'create_time', 'room_id')


class RoomSearch(ModelForm):
    class Meta:
        model = Room
        fields = ['guest_id', 'target', 'language']
