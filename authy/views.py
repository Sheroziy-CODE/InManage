from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.urls import reverse
from authy.forms import ProfileForm, StaffCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.http import JsonResponse
import json 

def login_page(request):
    return render(request, 'authy/login.html')

def login_view(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('username')
        password = data.get('password')
        user = authenticate(request, username=username, password=password)

        if not user:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
        login(request, user)

        return JsonResponse({'redirectUrl': reverse('workers')})

@login_required
def profile_view(request, username):
    # the username is added in here just to make the url dynamic
    form = ProfileForm(request.POST or None, request.FILES or None, instance=request.user.profile)
    if request.method == 'POST':
        if form.is_valid():
            profile = form.save(commit=False)
            profile.save()
    return render(request, 'authy/profile.html', {'form': form})

@login_required
def workers_view(request):
    users = User.objects.exclude(id=request.user.id)
    search = request.GET.get('search')
    if search:
        users = users.filter(username__icontains=search)

    if request.method == 'POST':
        form = StaffCreateForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = StaffCreateForm()

    groups = Group.objects.all()

    context = {'users': users, 'form': form, 'groups': groups}
    
    return render(request, 'authy/workers.html', context)