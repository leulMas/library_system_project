from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import AdminUserCreationForm

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def users_list(request):
    users = User.objects.all()
    return render(request, 'users_list.html', {'users': users})

def users_create(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        User.objects.create(username=username, email=email)
        return redirect('users_list')
    return render(request, 'users_form.html')

def users_edit(request, pk):
    user = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        user.username = request.POST['username']
        user.email = request.POST['email']
        user.save()
        return redirect('users_list')
    return render(request, 'users_form.html', {'user': user})

def users_delete(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()
    return redirect('users_list')
    

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

def signup(request):
    if request.method == 'POST':
        form = AdminUserCreationForm(request.POST)

        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')

            user = authenticate(username=username, password=raw_password)
            if user:
                login(request, user)

            messages.success(request, f"User '{username}' created successfully!")
            form = AdminUserCreationForm()  # Clear form after success
        else:
            # This will display all form errors nicely in template
            messages.error(request, "Please fix the errors below.")

    else:
        form = AdminUserCreationForm()

    return render(request,'signup.html', {"form": form})
