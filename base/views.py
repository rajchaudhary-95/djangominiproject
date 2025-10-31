from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count          #Used for serach related operations.

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from .models import Room,Topic,Message,User
from .forms import RoomForm, UserForm, MyUserCreationForm, MessageForm     
# Create your views here.

def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        email = request.POST.get('email').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, "User does not exist")
        user = authenticate(request, email=email,password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password does not exist")
    context = {'page':page}
    return render(request,'base/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def registerPage(request):
    form = MyUserCreationForm()

    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)          #when form is valid the user is gonna get created so commit false makes access the user right away
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'An error occurred during registration')
    return render(request, 'base/login_register.html', {'form' : form})

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''

    # Filter rooms by topic, name, or description
    rooms = Room.objects.filter(
        Q(topics__name__icontains=q) |   # <-- updated for ManyToManyField
        Q(name__icontains=q) |
        Q(description__icontains=q)
    ).annotate(
        message_count=Count('messages', distinct=True),
        participant_count=Count('participants', distinct=True)
    ).order_by('-message_count', '-participant_count', '-created')

    topics = Topic.objects.all()  
    room_count = rooms.count()

    room_messages = Message.objects.filter(Q(room__topics__name__icontains=q)).distinct()[:4]

    context = {
        'rooms': rooms,
        'topics': topics,
        'room_count': room_count,
        'room_messages': room_messages
    }
    return render(request, 'base/home.html', context)

@login_required(login_url='login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.messages.all()
    participants = room.participants.all()

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.room = room
            message.save()
            room.participants.add(request.user)
            return redirect('room', pk=room.id)
    else:
        form = MessageForm()

    context = {
        'room': room,
        'room_messages': room_messages,
        'participants': participants,
        'form': form
    }
    return render(request, 'base/room.html', context)


def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()
    topics = Topic.objects.all()
    context ={'user': user, 'rooms':rooms,'room_messages':room_messages,'topics':topics}
    return render(request, 'base/profile.html', context)


@login_required(login_url='/login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_input = request.POST.get('topics', '')  # "Python, AI, Django"
        topic_names = [t.strip() for t in topic_input.split(',') if t.strip()]

        room = Room.objects.create(
            host=request.user,
            name=request.POST.get('name'),
            description=request.POST.get('description'),
        )

        for name in topic_names:
            topic, created = Topic.objects.get_or_create(name=name)
            room.topics.add(topic)
        return redirect('home')
    context = {'form': form,'topics':topics}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='/login')
def updateRoom(request,pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)     # Form will be prefilled with room value to edit that specific room
    topics = Topic.objects.all()
    if request.user != room.host:
        return HttpResponse("You are not allowed here!")

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, created = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.description = request.POST.get('description')
        room.save()
        return redirect('home')

    context={'form': form,'topics':topics, 'room':room}
    return render(request, 'base/room_form.html',context)

@login_required(login_url='/login')
def deleteRoom(request,pk):
    room = Room.objects.get(id=pk)

    if request.user != room.host:
        return HttpResponse("You are not allowed here!")
    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':room})

@login_required(login_url='/login')
def deleteMessage(request,pk):
    message = Message.objects.get(id=pk)

    if request.user != message.user:
        return HttpResponse("You are not allowed here!")
    if request.method == 'POST':
        message.delete()
        return redirect('home')
    return render(request,'base/delete.html',{'obj':message})


@login_required(login_url='/login')
def updateUser(request):
    user = request.user 
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST,request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile',pk=user.id)
    return render(request, 'base/update-user.html',{'form':form})

def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q')!=None else ''
    topics = Topic.objects.filter(name__icontains=q)
    return render(request,'base/topics.html',{'topics':topics})

def activityPage(request):
    room_messages = Message.objects.all()
    return render(request,'base/activity.html',{'room_messages': room_messages})