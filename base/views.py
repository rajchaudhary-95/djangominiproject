from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q          #Used for serach related operations.
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import Room,Topic
from .forms import RoomForm     #importing after making Roomform in forms.py
# Create your views here.

# rooms = [
#     {'id': 1, 'name':'lets learn python!'},
#     {'id': 2, 'name':'Design with me'},
#     {'id': 3, 'name':'Frontend dev'},
# ]

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User does not exist")
        user = authenticate(request, username=username,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password does not exist")
    context = {}
    return render(request,'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''      #if request has q variable then it filters but if none exist with such name then all are displayed. All button doenst have q therefore everything is displayed 
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q)|
        Q(description__icontains=q)
        )       #contains sees for eg if for searching python only py is added to sitename then it searches for rooms starting with py.(full python isnt needed to be typed) and icontains = case insensitive (contains)
                # by using Q we put OR for searching either room name or room topic or room description
    topics = Topic.objects.all()
    room_count = rooms.count()
    context = {'rooms':rooms,'topics':topics, 'room_count':room_count}
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