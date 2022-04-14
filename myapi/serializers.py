from rest_framework import serializers

from .models import Icecream

class IcecreamSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Icecream
        fields = ('id', 'type', 'amount')
