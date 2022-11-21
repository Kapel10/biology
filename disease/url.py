from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),

    path('diseasetypetable',views.diseasetypes,name="diseasetypetable"),

    path('diseasetype/<str:pk>/',views.diseasetype,name="diseasetype"),

    path('create-disasetype/',views.creatediseasetype,name="create-diseasetype"),
    path('update-disasetype/<str:pk>/',views.updatediseasetype,name="update-diseasetype"),
    path('delete-disasetype/<str:pk>/',views.deletediseasetype,name="delete-diseasetype"),
#####################################################################################################################
    path('country/<str:pk>/',views.country,name="country"),
    path('countrytable/',views.countries,name="countries"),

    path('create-country/',views.createcountry,name="create-country"),
    path('update-country/<str:pk>/',views.updatecountry,name="update-country"),
    path('delete-country/<str:pk>/',views.deletecountry,name="delete-country"),
#####################################################################################################################
    path('disease/<str:pk>/', views.disease, name="disease"),
    path('diseasetable/', views.diseases, name="diseasetable"),

    path('create-disease/', views.createdisease, name="create-disease"),
    path('update-disease/<str:pk>/', views.updatedisease, name="update-disease"),
    path('delete-disease/<str:pk>/', views.deletedisease, name="delete-disease"),
#####################################################################################################################
    path('discover/<str:pk>/', views.discover, name="discover"),
    path('discovertable/', views.discoveries, name="discovertable"),

    path('create-discover/', views.creatediscover, name="create-discover"),
    path('update-discover/<str:pk>/', views.updatediscover, name="update-discover"),
    path('delete-discover/<str:pk>/', views.deletediscover, name="delete-discover"),

#####################################################################################################################
    path('user/<str:pk>/', views.duser, name="user"),
    path('users/', views.dusers, name="users"),

    path('create-user/', views.createdusers, name="create-user"),
    path('update-user/<str:pk>/', views.updatedusers, name="update-user"),
    path('delete-user/<str:pk>/', views.deletedusers, name="delete-user"),
#####################################################################################################################
    path('publicservant/<str:pk>/', views.publicservant, name="publicservant"),
    path('publicservants/', views.publicservants, name="publicservants"),

    path('create-publicservant/', views.createpublicservant, name="create-publicservant"),
    path('update-publicservant/<str:pk>/', views.updatepublicservant, name="update-publicservant"),
    path('delete-publicservant/<str:pk>/', views.deletepublicservant, name="delete-publicservant"),
#####################################################################################################################
    path('doctor/<str:pk>/', views.doctor, name="doctor"),
    path('doctors/', views.doctors, name="doctors"),

    path('create-doctor/', views.createdoctor, name="create-doctor"),
    path('update-doctor/<str:pk>/', views.updatedoctor, name="update-doctor"),
    path('delete-doctor/<str:pk>/', views.deletedoctors, name="delete-doctor"),
#####################################################################################################################
    path('specialize/<str:pk>/', views.specialize, name="specialize"),
    path('specializes/', views.specializes, name="specializes"),

    path('create-specialize/', views.createspecialize, name="create-specialize"),
    path('update-specialize/<str:pk>/', views.updatespecialize, name="update-specialize"),
    path('delete-specialize/<str:pk>/', views.deletespecialize, name="delete-specialize"),
#####################################################################################################################
    path('record/<str:pk>/', views.record, name="record"),
    path('records/', views.records, name="records"),

    path('create-record/', views.createrecords, name="create-record"),
    path('update-record/<str:pk>/', views.updaterecords, name="update-record"),
    path('delete-record/<str:pk>/', views.deleterecord, name="delete-record"),
]
