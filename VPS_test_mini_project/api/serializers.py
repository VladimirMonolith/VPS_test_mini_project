from rest_framework import serializers

from vps.models import VPS


class VPSSerializer(serializers.ModelSerializer):
    '''Сериализатор для модели VPS.'''

    class Meta:
        model = VPS
        fields = ('uid', 'cpu', 'ram', 'hdd', 'status')
