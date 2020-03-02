from django.shortcuts import render, redirect, get_object_or_404, reverse
from .forms import UrlsShorterForm
from .models import ShortUrl


# Create your views here.

def index(request):
    form = UrlsShorterForm()
    urls = ShortUrl.objects.all()
    if request.method == 'GET':
        return render(request, 'urlshorter.html', context={'form': form, 'urls': urls})
    if request.method == 'POST':
        form = UrlsShorterForm(request.POST)
        if form.is_valid():
            notshorter_url = form.cleaned_data.get('url')
            if form.cleaned_data.get('link'):
                new_cut = ShortUrl.objects.create(notshorter_url=notshorter_url, link=form.cleaned_data.get('link'))
                return redirect(reverse('urlsorter'))
            else:
                new_cut = ShortUrl.objects.create(notshorter_url=notshorter_url)

            return redirect(reverse('urlsorter'))
        else:
            return render(request, 'urlshorter.html', context={'form': form, 'urls': urls})


def redirect_view(request, link):
    if request.method == 'GET':
        current_url = ShortUrl.objects.get(link=link)
        current_url.clicks += 1
        current_url.save()
        redirect_url = current_url.notshorter_url
        return redirect(redirect_url)
