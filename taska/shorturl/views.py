import string
import random
import logging

from django.shortcuts import render, redirect

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
                if not Urls.objects.filter(url=form.cleaned_data['url'], user=request.user).exists():
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


def history_list(request):
    if request.user.is_authenticated:
        url = Urls.objects.filter(user=request.user)
        return render(request, "main/history.html", {"url": url})
    else:
        return redirect('/login/', )
