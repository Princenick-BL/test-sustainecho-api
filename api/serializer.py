from rest_framework import serializers
from .models import Employés,Pays,Ville,Marques

class PaysSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pays
        fields = ('id','nom')

class VilleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ville
        fields = ('id','nom','pays')

class MarqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marques
        fields = ('id','nom')
   
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employés
        fields = ('id','nb_employe','marque','ville')
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['marque'] = MarqueSerializer(instance.marque).data
        rep['ville'] = MarqueSerializer(instance.ville).data

        return rep
        