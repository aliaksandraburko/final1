from django.db import models
import random
import string


def code_gen():
    elements = string.ascii_lowercase + string.digits
    link = ''.join(random.choice(elements) for x in range(5))
    return link


class ShortUrl(models.Model):
    link = models.CharField(max_length=5, default=code_gen)
    notshorter_url = models.URLField()
    created = models.DateTimeField(auto_now_add=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return f'id: {self.id}, link: {self.link}'

    class Meta:
        ordering = ['clicks']
