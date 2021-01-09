from django.views.generic.base import TemplateView
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, redirect, HttpResponse
from .forms import GameSelectForm, RoomCreate, RoomSearch
from django.urls import reverse
from .models import Game, GameType, Platform, Series, Language, Company, Target, Room
from random import randint

# Create your views here.


# class HomeView(TemplateView):
#
#     template_name = 'PostAndSearch/homepage.html'
#
#     def get_context_data(self, **kwargs):
#         context['']
#         game = Game.objects.get(pk=3)
#         all_game = Game.objects.all()
#         all_game_new = Game.objects.all().order_by('-release_date')
#         return render(request, 'PostAndSearch/homepage.html',
#                       context={'all_game': all_game,
#                                'all_game_new': all_game_new,
#                                'game': game,
#                                })

def homepage(request):
    if request.method == 'POST':
        game_name = request.POST.get('selected_game').replace(' ', '-')
        return redirect('/homepage/game/{}/'.format(game_name))

    else:
        games = Game.objects.all()
        args = {
            'games': games}
        return render(request, 'PostAndSearch/homepage.html', args)


def match_room(request, english_name):
    if request.method == 'POST':

        random_room_id = randint(100000, 999999)
        game = Room(game=english_name, room_id=random_room_id)
        create_form = RoomCreate(request.POST, instance=game)

        if create_form.is_valid():
            create_form.save()
            exist_rooms = Room.objects.filter(game=english_name).order_by('create_time')
            args = {
                'exist_rooms': exist_rooms,
                'create_form': create_form,
            }
            return redirect('{}/'.format(random_room_id))

    else:
        if request.GET.get('search'):
            exist_rooms = Room.objects.filter(target=request.GET['target'], language=request.GET['language'])
            create_form = RoomCreate()
            search_form = RoomSearch()
            title = english_name
            game = Game.objects.filter(english_name=english_name)

            args = {
                'exist_rooms': exist_rooms,
                'title': title,
                'game': game,
                'create_form': create_form,
                'search_form': search_form,
                'english_name': english_name,
            }

            return render(request, 'PostAndSearch/MatchingPage.html', args)

        else:
            exist_rooms = Room.objects.filter(game=english_name).order_by('create_time')
            create_form = RoomCreate()
            search_form = RoomSearch()
            title = english_name
            game = Game.objects.filter(english_name=english_name)

            args = {
                'exist_rooms': exist_rooms,
                'title': title,
                'game': game,
                'create_form': create_form,
                'search_form': search_form,
                'english_name': english_name,
            }

            return render(request, 'PostAndSearch/MatchingPage.html', args)


def chat_room(request, english_name, room_id):
    if Room.objects.filter(room_id=room_id):
        arg = {
            'room_id': room_id,
            'english_name': english_name,
        }
        return render(request, 'PostAndSearch/private_page.html', arg)
    else:
        return HttpResponse('Room does not exist')


def home_index(request):
    if request.method == 'POST':
        form = GameSelectForm(request.POST, instance=request.game)
        if form.is_valid():
            redirect_url = request.game

            return redirect('/search/{}'.format(redirect_url))

    else:
        search_form = GameSelectForm(request.game)
        context = {'search_form': search_form}
        return render(request, 'PostAndSearch/MainPage', context)


def home(request):
    game = Game.objects.get(pk=3)
    all_game = Game.objects.all()
    all_game_new = Game.objects.all().order_by('-release_date')
    return render(request, 'PostAndSearch/homepage.html',
                  context={'all_game': all_game,
                           'all_game_new': all_game_new,
                           'game': game,
                           })


def home_redirect_search(request, game_id):
    selected_game = Game.objects.get(pk=game_id)
    return redirect('home', id=game_id)


def search(request, id):
    game = Game.objects.filter(pk=id)
    return render(request, 'PostAndSearch/MatchingPage.html',
                  context={'game': game,
                           })