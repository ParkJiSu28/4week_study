from rest_framework import serializers
from .models import Exmodel


class ExmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exmodel
        fields =('title','content')
        read_only_fields=('create',)
