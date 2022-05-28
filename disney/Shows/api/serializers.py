from pyexpat import model
from attr import fields
from rest_framework import serializers
from Shows.models import Show


class Showserializers(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Show 