from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
# this is our custom form
# from .forms import TodoForm
from .forms import WeekForm
from django.contrib import messages

# Create your views here.
# from .models import Todo
from .models import Week

# from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    if request.method == "GET":
        return render(request, 'todo/home.html', {'form': AuthenticationForm()})
    else:
        # must be a POST request from the login form
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), "error": "Username and password did not match"})
        else:
            login(request, user)
            # need to send this user somewhere
            # currentodos right below is using the NAME from the url.py
            return redirect('allweeks')



def signupuser(request):
    if request.method == "GET":
        # just visiting a url is a GET request so this will just send them to
        # the page
        return render(request, 'todo/signupuser.html', {'form': UserCreationForm()})
    else:
        # this must be a post coming from the signupuser.html page.  The form
        # is set to not go anywhere but say on same page.
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save
                login(request, user)
                # need to send this user somewhere
                # currentodos right below is using the NAME from the url.py
                return redirect('allweeks')

            # look at django error code and see the type of error when username is already in databas
            # it is an IntegrityError
            except IntegrityError:
                return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken.  Please choose a new username'})

        else:
            # no magic to the dictionary key being named error.  can use anything
            return render(request, 'todo/signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})
            # tell user the passwords didn't match

@login_required
def allweeks(request):
    # only display current todos for the current user. also filtered by uncompleted
    # we can list as many filters as we want in the arguments.
    weeks = Week.objects.filter(user=request.user).order_by('-week')
    return render(request, 'todo/allweeks.html', {'weeks': weeks})

# @login_required
# def completedtodos(request):
#     todos = Todo.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
#     return render(request, 'todo/completedtodos.html', {'todos': todos})

@login_required
def viewweek(request, week_pk):
    # only display current todos for the current user. also filtered by uncompleted
    # we can list as many filters as we want in the arguments.
    week = get_object_or_404(Week, pk=week_pk, user=request.user)
    if request.method == 'GET':
        form = WeekForm(instance=week)
        return render(request, 'todo/viewweek.html', {'week': week, 'form': form})
    else:
        try:
            # The instance = todo indicates we are updating an instance
            form = WeekForm(request.POST, instance = week)
            form.save()
            return redirect('allweeks')
        except ValueError:
            return render(request, 'todo/viewweek.html', {'week': week, 'form': form, 'error': 'Bad Info'})

@login_required
def logoutuser(request):
    # this must be included so its not a GET request and preloaded by browswers
    # the user will constantly be logged out. make sure the link that gets sent
    # here is NOT an a tag.  must be a form for the post request.
    if request.method == 'POST':
        logout(request)
        return redirect("home")


def loginuser(request):
    if request.method == "GET":
        return render(request, 'todo/loginuser.html', {'form': AuthenticationForm()})
    else:
        # must be a POST request from the login form
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'todo/loginuser.html', {'form': AuthenticationForm(), "error": "Username and password did not match"})
        else:
            login(request, user)
            # need to send this user somewhere
            # currentodos right below is using the NAME from the url.py
            return redirect('allweeks')

@login_required
def createweek(request):
    if request.method == "GET":
        return render(request, 'todo/createweek.html', {'form': WeekForm()})

    else:
        try:
            # don't have to reference all the fiels from the posts
            # individually..Django matches them up


            form = WeekForm(request.POST)
            newweek = form.save(commit=False)
            newweek.user = request.user
            newweek.save()
            return redirect('allweeks')
        except ValueError:
            return render(request, 'todo/createweek.html', {'form': form, "error": "Bad or missing data. You must enter text for every day."})

# @login_required
# def completetodo(request, week_pk):
#     todo = get_object_or_404(Todo, pk=week_pk, user=request.user)
#     if request.method == 'POST':
#         todo.datecompleted = timezone.now()
#         todo.save()
#         return redirect('currentodos')

@login_required
def deleteweek(request, week_pk):
    week = get_object_or_404(Week, pk=week_pk, user=request.user)
    if request.method == 'POST':
        week.delete()
        return redirect('allweeks')
