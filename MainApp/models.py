from django.db import models
from django.contrib.auth.models import User

LANGS = (
    ('py', 'Python'),
    ('js', 'JavaScript'),
    ('cpp', 'C++'),
    ('html', 'HTML')
)


class Snippet(models.Model):
    name = models.CharField(max_length=100)
    lang = models.CharField(max_length=30, choices=LANGS)
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(to=User,
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE)
    public = models.BooleanField(default=True)
