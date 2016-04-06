from django.shortcuts import render, get_object_or_404
from urllib.parse import quote_plus
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import AuthorForm, LoginForm
from .models import Author
# Create your views here.


def register_author(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect("/posts/")  # for now
    form = AuthorForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        user = User.objects.create_user(username=form.cleaned_data['email'],
                                        email=form.cleaned_data['email'],
                                        password=form.cleaned_data['password'],
                                        first_name=form.cleaned_data['first_name'],
                                        last_name=form.cleaned_data['last_name'],)
        user.save()
        instance = form.save(commit=False)
        instance.user = request.user
        instance.save()
        # message success
        messages.success(request, 'User created')
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "form": form,
    }
    return render(request, "blog/signup.html", context)


def log_in(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
               
                return HttpResponseRedirect("/posts/")
            else:
               
                return render(request, "blog/signup.html")

        else:
           
            return render(request, "blog/login.html")
    context = {
        'form': form
         }
    return render(request, "blog/login.html", context)


def log_out(request):
    logout(request)
    return HttpResponseRedirect("/")

def profile(request, slug=None):
    instance = get_object_or_404(Author, slug=slug)
    share_string = quote_plus(instance.email)
    context = {
        "email": instance.email,
        "first_name": instance.first_name,
        "last_name": instance.last_name,
        "share_string": share_string,
        "avatar": instance.avatar,
    }
    return render(request, "blog/profile.html", context)



