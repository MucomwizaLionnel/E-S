
from django.urls import path
from .import views 



urlpatterns = [

    path('',views.index ,name="index" ),
    path('login/',views.login_view ,name='login_view' ),
    path('register/',views.register ,name='register' ),
    path('home/',views.home,name='home' ),
    path('comptable/',views.comptable,name='comptable' ),
    path('chef/',views.chef,name='chef' ),
    path('chef_equipe/',views.responsable,name='responsable' ),
    path('tache/',views.tache,name='tache' ),
    path('envoy/',views.envoy,name='envoy' ),
    path('envoyrec/',views.envoyrec,name='envoyrec' ),
    path('update/<int:id>',views.update,name="update"),
    path('update/uprec/<int:id>',views.uprec,name="uprec"),
    path('supprimer/<int:id>/',views.supprimer,name="supprimer"),
    path('transaction/',views.transaction,name='transaction' ),
    path('produit/',views.produit,name='produit' ),
    path('prestation/',views.prestation,name='prestation' ),
    path('charge/',views.charge,name='charge' ),
    path('marche/',views.marche,name='marche' ),
     path('stock/',views.stock,name='stock' ),



]