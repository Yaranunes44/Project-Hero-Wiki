from rest_framework import serializers


class UniversoSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nome = serializers.CharField()


    def create(self, validated_data):
        habilidade_data = validated_data.pop('hab_heroi')
        habilidade = Habilidade.objects.get(id=habilidade_data['id'])


