import string
import random
import logging

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from shorturl.models import Urls
from shorturl.forms import AddUrlForm

logger = logging.getLogger(__name__)


def home(request):
    all_urls = Urls.objects.all()
    return render(request, "main/main.html", {'all_urls': all_urls})


def short_url(request):
    char = string.ascii_uppercase + string.digits + string.ascii_lowercase
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddUrlForm(request.POST)
            if form.is_valid():
                logger.info(form.cleaned_data)
                new_url = Urls.objects.create(url=form.cleaned_data['url'],
                                              short=''.join(random.choice(char) for x in range(9)),
                                              user=request.user)
                new_url.save()
            return redirect('/')
        else:
            form = AddUrlForm()
    else:
        return redirect('/login/', )
    return render(request, 'main/form.html', {'form': form})


# def url_redirect(request, slug):
#     return redirect(Urls.objects.get(short=slug).url)


def history_list(request):
    if request.user.is_authenticated:
        url = Urls.objects.filter(user=request.user)
        return render(request, "main/history.html", {"url": url})
    else:
        return redirect('/login/', )
