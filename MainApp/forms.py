from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from MainApp.models import Snippet


class SnippetForm(ModelForm):
    class Meta:
        model = Snippet
        # Описываем поля, которые будем заполнять в форме
        fields = ['name', 'lang', 'code', 'public']
        labels = {'name': '', 'lang': '', 'code': '', 'public':'Публичный'}
        widgets = {
          'name': TextInput(
              attrs={"class":"form-control", 'style': 'max-width: 350px;', 'placeholder': 'Название сниппета'}
              ),
          'code': Textarea(
              attrs={"class":"form-control", 'style': 'max-width: 350px;', 'placeholder': 'Код сниппета'}
              ),
           'public': CheckboxInput(
              attrs={"class":"form-control", 'style': 'width: 50px;'}
              ),
        }