from rest_framework import serializers
#from drf_extra_fields.fields import Base64ImageField

from .models import Pais
from .models import Universidad
from .models import Institucion
from .models import PlanEstudio
from .models import Guia
from .models import NodoCurso
from .models import NodoModCurso
from .models import EnlaceCurso
from .models import EnlaceModCurso

from .comparadata import *


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = ['id', 'nombre',]

class UniversidadSerializer(serializers.ModelSerializer):
    paises = PaisSerializer(many=True, read_only=True)
    class Meta:
        model = Universidad
        fields = ['id','nombre','paises',]

class InstitucionSerializer(serializers.ModelSerializer):
    paises = PaisSerializer(many=True, read_only=True)
    class Meta:
        model = Institucion
        fields = ['id', 'nombre', 'paises',]

class PlanEstudioSerializer(serializers.ModelSerializer): 
    universidades =  UniversidadSerializer(many=True, read_only=True)
    class Meta:
        model = PlanEstudio
        fields = ['id', 'nombre', 'fecha_vigencia', 'universidades',]

class GuiaSerializer(serializers.ModelSerializer): 
    instituciones =  InstitucionSerializer(many=True, read_only=True)
    class Meta:
        model = Guia
        fields = ['id', 'nombre', 'fecha_vigencia', 'instituciones',]


class NodoCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodoCurso
        fields = ['id','name', 'plan',]


class NodoModCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = NodoModCurso
        fields = ['id','name', 'guia',]


class EnlaceModCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnlaceModCurso
        fields = ['origen', 'destino', 'guia',]


class EnlaceCursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = EnlaceCurso
        fields = ['origen', 'destino', 'plan',]


class GrafoSerializer(serializers.Serializer):
    nodos = serializers.IntegerField()
    enlaces = serializers.IntegerField()

class ComparaGraphSerializer(serializers.Serializer):
    # campos del modelo de respuesta
    grafoG =  GrafoSerializer()
    grafoH = GrafoSerializer()
    MCS = GrafoSerializer()
    ged = serializers.DecimalField(max_digits=5, decimal_places=2)
    image = serializers.CharField()

