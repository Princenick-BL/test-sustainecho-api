from django.db import models

# Create your models here.
class Pays(models.Model):
    nom = models.CharField(max_length=60)
    def __str__(self):
        return self.nom

class Ville(models.Model):
    nom = models.CharField(max_length=60)
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE)
    def __str__(self):
        return  self.nom

class Marques(models.Model):
    nom = models.CharField(max_length=60)
    def __str__(self):
        return  self.nom

class Employés(models.Model):
    nb_employe = models.IntegerField()
    marque = models.ForeignKey(Marques, on_delete=models.CASCADE)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE)
    def __str__(self):
        return "marque :"+ str(self.marque) +  " ville :"+ str(self.ville) + " "+str(self.nb_employe)+" employé(s)"

