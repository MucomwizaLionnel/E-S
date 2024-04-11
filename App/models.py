from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User 
from datetime import datetime;

class Chef(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE,related_name="chef_user")
    birthday =models.DateField(default=datetime.now)
    gender =models.CharField(max_length=100)
    phone =models.CharField(max_length=100)
    address=models.CharField(max_length=100, null = True)  

class Comptable(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE,related_name="comptable_user")
	birthday =models.DateField(default=datetime.now)
	gender =models.CharField(max_length=100, null = True)
	phone =models.CharField(max_length=100, null = True)
	address=models.CharField(max_length=100, null = True) 

class responsable(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,related_name="responsable_user")
	birthday =models.DateField(default=datetime.now)
	gender =models.CharField(max_length=100, null = True)
	phone =models.CharField(max_length=100, null = True)
	address=models.CharField(max_length=100, null = True)     

class Techniciens(models.Model):
    nom=models.CharField(max_length=100)
    prenom=models.CharField(max_length=100)
    adresse=models.CharField(max_length=100)
    telephone=models.CharField(max_length=100)
    dateembauch=models.DateField()
    fonction=models.CharField(max_length=100)
    salaire=models.IntegerField()

class Tache(models.Model):
    date=models.DateField()
    technicien=models.ForeignKey(Techniciens,on_delete=models.CASCADE, null=True)
    titre=models.CharField(max_length=150)
    description=models.TextField(max_length=1000)

class Equipe(models.Model):
    nom=models.CharField(max_length=100)
    membres=models.CharField(max_length=100)
    datedebit=models.DateField()
    datefin=models.DateField()
    lieu=models.CharField(max_length=100)
  

class Stock(models.Model):
    nomproduit=models.CharField(max_length=100)
    datecreation=models.DateField()
    
    dateexp=models.DateField()
    dateentree=models.DateTimeField()
   
    lots=models.CharField(max_length=100)
    pu=models.IntegerField()
    quantite=models.IntegerField()
    pt=models.IntegerField()

    commentaire=models.CharField(max_length=100)

    
    

    commentaire=models.IntegerField()

class Produit(models.Model):
    nomproduit=models.CharField(max_length=100)
    

    dateinscri=models.DateField()