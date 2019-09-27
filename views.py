# -*- coding: utf-8 -*-
# czat/views.py

from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    """Strona główna aplikacji."""
    # return HttpResponse("Witaj w aplikacji Czat!")
    return render(request, 'czat/index.html')

from django.contrib.auth import login, logout
from django.shortcuts import redirect
from django.core.urlresolvers import reverse
from django.contrib import messages

def loguj(request):
    """Logowanie użytkownika"""
    from django.contrib.auth.forms import AuthenticationForm
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            login(request, form.get_user())
            messages.success(request, "Zostałeś zalogowany!")
            return redirect(reverse('czat:index'))

    kontekst = {'form': AuthenticationForm()}
    return render(request, 'czat/loguj.html', kontekst)


def wyloguj(request):
    """Wylogowanie użytkownika"""
    logout(request)
    messages.info(request, "Zostałeś wylogowany!")
    return redirect(reverse('czat:index'))
