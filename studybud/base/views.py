from django.shortcuts import render

# Create your views here.


from django.http import HttpRequest, HttpResponse
from .models import Room, Topic, Message

# def home(request):
#     return HttpResponse('Home')

# rooms = [
#     {'id': 1, 'name': 'learn python 2'},
#     {'id': 2, 'name': 'basic design 2'},
#     {'id': 3, 'name': 'front end development'},
#     {'id': 4, 'name': 'backend development'},
# ]


def home(request):

    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

# def room(request):
#     return HttpResponse('Room')


def room(request, pk):

    # selectedroom = None
    # for room in rooms:
    #     if room['id'] == int(pk):
    #         selectedroom = room
    #         break

    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'room.html', context)
