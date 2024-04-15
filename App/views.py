from django.shortcuts import render,redirect
from django.contrib.auth.models import Group
# from .forms import ProfileForm,LoginForm,FormTache
from django.contrib.auth import authenticate,login
from .models import Tache, responsable

from .forms import *


def index(request):
    return render(request, 'index.html')

def register(request):
    profil_form=ProfileForm(request.POST or None, request.FILES)
    if (request.method=='POST'):
        if (profil_form.is_valid()):
            username=profil_form.cleaned_data['username']
            password=profil_form.cleaned_data['password']
            password1=profil_form.cleaned_data['password1']
            nom=profil_form.cleaned_data['nom']
            prenom=profil_form.cleaned_data['prenom']
            birthday=profil_form.cleaned_data['birthday']
            gender=profil_form.cleaned_data['gender']
            phone=profil_form.cleaned_data['phone']
            address=profil_form.cleaned_data['address']
            if (password==password1):
                user=User.objects.create_user(username=username, password=password)
                user.first_name=nom
                user.last_name=prenom
                user.save()
                group = Group.objects.get_or_create(name= "is_chef_Equip")
                user.groups.add(group[0])
                profil=responsable(
                        user=user,
						birthday=birthday,
						gender=gender,
						address=address,
						phone=phone).save()
                if user:
                    login(request, user)
                    return redirect(index)
                else:
                    return redirect(login_view)
            else: 
                profil_form=ProfileForm(request.FILES)
                return render(request, 'register.html',locals())
    return render(request, 'register.html',locals())
    

    # msg=None
    # if request.method=='POST':
    #     form=ProfileForm(request.POST)
    #     if form.is_valid():
    #         user=form.save()
    #         msg='user created'
            
    #         return redirect('login_view')
    #     else:
    #         msg='form is not valid'
    # else:
    #     form=ProfileForm()
    # return render(request,'register.html',{'form':form,'msg':msg})

def login_view(request):
    Connexion_form=ConnexionForm(request.POST or None)
    msg=None
    if request.method=='POST':
        if Connexion_form.is_valid():
            username=Connexion_form.cleaned_data.get('username')
            password=Connexion_form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)


            if user:#si l'objet existe 


                login(request, user)
                groups = [group.name for group in user.groups.all()]
                if user.is_superuser or 'comptable' in groups:
                    return redirect(comptable) #on connecte l'utilisateur
                if 'chef' in groups:
                    return redirect(chef) #on connecte l'utilisateur
                if 'is_chef_Equip' in groups:
                    return redirect(responsables) #on connecte l'utilisateur
                
            
            else:
                Connexion_form=ConnexionForm()
        else:
            Connexion_form=ConnexionForm()
            return render(request, 'login.html', locals())
    return render(request, 'login.html', locals())
        
def home(request):
    return render(request,'homepage.html')
  
def comptable(request):
    return render(request,'comptable.html')
    
def chef(request):
    return render(request,'chef.html')
 
def responsables(request):
    return render(request,'chef_equipe.html')    
def stock(request):
    return render(request,'stock.html') 
def tache(request):
    tach=Tache.objects.all()
    return render(request,'tache.html',{'tach':tach})           
def envoy(request):
    return render(request,'envoy.html')   
def envoyrec(request):
    tache_form=tacheform(request.POST or None)
    if (request.method=='POST'):
        if (tache_form.is_valid()):
            tache_form.save()
            return redirect('/') 
        return render(request, 'envoy.html',locals())
    return render(request, 'envoy.html',locals())

def supprimer(request,id):
    tache=Tache.objects.get(id=id)
    tache.supprimer()
    return redirect("")


def update(request,id):
    tache=Tache.objects.get(id=id)
    return render(request,'update.html',{'tache':tache})

def uprec(request,id):
    x=request.POST['date']
    y=request.POST['technicien']
    z=request.POST['titre']
    w=request.POST['description']
    tache=Tache.objects.get(id=id)
    tache.date=x
    tache.technicien=y
    tache.titre=z
    tache.description=w
    tache.save()
    return redirect("/")

def marche(request):
    return render(request,'marche.html') 
def prestation(request):
    return render(request,'prestation.html') 
def produit(request):
    return render(request,'produit.html') 
def transaction(request):
    return render(request,'transaction.html') 
def charge(request):
    return render(request,'charge.html') 


def tache(request):
    tache_form=tacheform(request.POST or None, request.FILES)
    if (request.method=='POST'):
        if (tache_form.is_valid()):
            date=tache_form.cleaned_data['date']
            technicien=tache_form.cleaned_data['technicien']
            titre=tache_form.cleaned_data['titre']
            description=tache_form.cleaned_data['description']
           