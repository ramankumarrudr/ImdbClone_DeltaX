from django import forms
from django.core import validators
from .models import Movie,Actor,Tvshow
class UserForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields =  ('movie','movie_actor','lang','gener','status','release_date','plot','movie_image')
class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = ('actor','sex','DOB','Bio','actor_image')

class TvshowForm(forms.ModelForm):
    class Meta:
        model = Tvshow
        fields =  ('tvshow','tv_actor','lang','gener','status','release_date','plot','tvshow_image')


     