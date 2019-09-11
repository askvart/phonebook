from django.forms import ModelForm

from .models import Tt

class TtForm(ModelForm):
    class Meta:
        model = Tt
        fields = ('family', 'content', 'nomer', 'rubric')


