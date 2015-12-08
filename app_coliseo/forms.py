from django import forms

from .models import MyModel
from .models import Persona,Campeonato,Equipo,Jugador,Partido,PartidoAnotacion,PartidoArbitro

class MyModel(forms.ModelForm):

    class Meta:

        model = MyModel
        fields = ('title', )

class ModelPersona(forms.ModelForm):
	class Meta:
		model = Persona
		fields = '__all__'


class ModelCampeonato(forms.ModelForm):
	class Meta:
		model = Campeonato
		fields = '__all__'


class ModelEquipo(forms.ModelForm):
	class Meta:
		model = Equipo
		fields = '__all__'


class ModelJugador(forms.ModelForm):
	class Meta:
		model = Jugador
		fields = '__all__'

class ModelPartido(forms.ModelForm):
	class Meta:
		model = Partido
		fields = '__all__'

class ModelPartidoAnotacion(forms.ModelForm):
	class Meta:
		model = PartidoAnotacion
		fields = '__all__'

class ModelPartidoArbitro(forms.ModelForm):
	class Meta:
		model = PartidoArbitro
		fields = '__all__'

		##djaneiro