from rest_framework import serializers
from habilidades.models import Habilidade


class HabilidadeSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField()