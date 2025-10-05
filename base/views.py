from django.shortcuts import render, redirect
from .models import Room
from .forms import RoomForm     #importing after making Roomform in forms.py
# Create your views here.

# rooms = [
#     {'id': 1, 'name':'lets learn python!'},
#     {'id': 2, 'name':'Design with me'},
#     {'id': 3, 'name':'Frontend dev'},
# ]

def home(request):
    rooms = Room.objects.all()
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request,pk):
    room = Room.objects.get(id=pk)
    context  = {'room':room}

    return render(request, 'base/room.html', context)

def createRoom(request):
    form = RoomForm()

    if request.method == 'POST':
        form = RoomForm(request.POST)      # passing in all the POST data in the form
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {'form': form}
    return render(request, 'base/room_form.html', context)


def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)     # Form will be prefilled with room value to edit that specific room

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)        #Specifying which room to update
        if form.is_valid():
            form.save()
            return redirect('home')

    context={'form': form}
    return render(request, 'base/room_form.html',context)

def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})