from django import forms
from .models import ShortUrl
from django.core.exceptions import ValidationError


class UrlsShorterForm(forms.Form):
    url = forms.URLField(label='url')


    def clean_code(self):
        urls = ShortUrl.objects.all()
        link = self.cleaned_data.get('link')
        short_urls = []
        for obj in urls:
            short_urls.append(obj.link)
        if link in short_urls:
            raise ValidationError('this link is in use')
        return link