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
    lang = models.CharField(max_length=30, choices=LANGS, verbose_name="Язык")
    code = models.TextField(max_length=5000)
    creation_date = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(to=User,
                             blank=True,
                             null=True,
                             on_delete=models.CASCADE)
    public = models.BooleanField(default=True) # True = public, False = private

    def __repr__(self) -> str:
        return f"snippet({self.name},{self.lang})"
    
    def __str__(self):
        return self.name
    
