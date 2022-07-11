import string
import random

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from shorturl.models import Urls
from shorturl.forms import UrlForm


def home(request):
    all_urls = Urls.objects.all()
    return render(request, "main/main.html", {'all_urls': all_urls})


def short_url(request):
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    if request.method == 'POST':
        form = UrlForm(request.POST)
        if form.is_valid():
            url_from_html = form.cleaned_data['url']
            new_url = Urls.objects.create(
                url=url_from_html,
                short=''.join(random.choice(char) for x in range(9)))
            new_url.save()
            return reverse('home')
    else:
        form = Urls()
    return render(request, 'main/form.html')


def url_redirect(request, slug):
    return redirect(Urls.objects.get(shorter_url=slug).url)
