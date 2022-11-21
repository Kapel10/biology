from django.shortcuts import render,redirect
from .models import Diseasetype,Country,Disease,Discover,Users,Publicservant,Doctor,Specialize,Record
# Create your views here.
from .forms import DiseasetypeForm,CountryForm,DiseaseForm,DiscoverForm,UsersForm,PublicServantForm,DoctorForm,SpecializeForm,RecordForm


def home(request):
    diseasetypes = Diseasetype.objects.all()
    countr = Country.objects.all()
    diseas = Disease.objects.all()
    discov = Discover.objects.all()

    context = {
        'diseasetypes': diseasetypes,
        'countr' : countr,
        'diseas' : diseas,
        'discov': discov,

    }
    return render(request,'index.html',context)
#####################################################################################################################
def diseasetype(request,pk):
    disease_type = Diseasetype.objects.get(id=pk)
    context = {'disease_type':disease_type}
    return render(request, 'diseasetype.html',context)

def diseasetypes(request):
    diseasetypes = Diseasetype.objects.all()
    context = {
        'diseasetypes': diseasetypes
    }
    return render(request,'disease/diseasetype_table.html',context)


def creatediseasetype(request):
    form = DiseasetypeForm
    if request.method == 'POST':
        form = DiseasetypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diseasetypetable')
    context = {'form': form}
    return render(request,'disease/diseasetype_form.html',context)



def updatediseasetype(request,pk):
    disease_type = Diseasetype.objects.get(id=pk)
    form = DiseasetypeForm(instance=disease_type)
    if request.method == 'POST':
        form = DiseasetypeForm(request.POST,instance=disease_type)
        if form.is_valid():
            form.save()
            return redirect('diseasetypetable')
    context = {'form' : form}
    return render(request, 'disease/diseasetype_form.html',context)


def deletediseasetype(request,pk):
    disease_type = Diseasetype.objects.get(id=pk)
    if request.method == 'POST':
        disease_type.delete()
        return redirect('diseasetypetable')
    context = {'obj': disease_type}
    return render(request,'disease/delete.html',context)

#####################################################################################################################
def country(request,pk):
    countr = Country.objects.get(cname=pk)
    context = {'countr': countr}
    return render(request, 'country.html',context)

def countries(request):
    countr = Country.objects.all()
    context = {
        'countr': countr
    }
    return render(request,'disease/countries_table.html',context)

def createcountry(request):
    form = CountryForm
    if request.method == 'POST':
        form = CountryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('countries')
    context = {'form': form}
    return render(request,'disease/country_form.html',context)



def updatecountry(request,pk):
    countr = Country.objects.get(cname=pk)
    form = CountryForm(instance=countr)
    if request.method == 'POST':
        form = CountryForm(request.POST,instance=countr)
        if form.is_valid():
            form.save()
            return redirect('countries')
    context = {'form': form}
    return render(request, 'disease/country_form.html', context)


def deletecountry(request,pk):
    countr = Country.objects.get(cname=pk)
    if request.method == 'POST':
        countr.delete()
        return redirect('countries')
    context = {'obj': countr}
    return render(request,'disease/delete.html',context)

#####################################################################################################################

def disease(request,pk):
    diseas= Disease.objects.get(disease_code=pk)
    context = {'diseas':diseas}
    return render(request, 'disease.html',context)

def diseases(request):
    diseases = Disease.objects.all()
    context = {
        'diseases': diseases
    }
    return render(request,'disease/diseasetable.html',context)


def createdisease(request):
    form = DiseaseForm
    if request.method == 'POST':
        form = DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('diseasetable')
    context = {'form': form}
    return render(request,'disease/disease_form.html',context)



def updatedisease(request,pk):
    diseas = Disease.objects.get(disease_code=pk)
    form = DiseaseForm(instance=diseas)
    if request.method == 'POST':
        form = DiseaseForm(request.POST,instance=diseas)
        if form.is_valid():
            form.save()
            return redirect('diseasetable')
    context = {'form' : form}
    return render(request,'disease/disease_form.html',context)


def deletedisease(request,pk):
    diseas= Disease.objects.get(disease_code=pk)
    if request.method == 'POST':
        diseas.delete()
        return redirect('diseasetable')
    context = {'obj': diseas}
    return render(request,'disease/delete.html',context)

#####################################################################################################################

def discover(request,pk):
    discove = Discover.objects.get(id=pk)
    context = {'discove': discove}
    return render(request, 'discover.html',context)

def discoveries(request):
    discover = Discover.objects.all()
    context = {
        'discover': discover
    }

    return render(request,'disease/discoveries.html',context)


def creatediscover(request):
    form = DiscoverForm
    if request.method == 'POST':
        form = DiscoverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('discovertable')
    context = {'form': form}
    return render(request,'disease/discover_form.html',context)



def updatediscover(request,pk):
    discov = Discover.objects.get(id=pk)
    form = DiscoverForm(instance=discov)
    if request.method == 'POST':
        form = DiscoverForm(request.POST,instance=discov)
        if form.is_valid():
            form.save()
            return redirect('discovertable')
    context = {'form' : form}
    return render(request,'disease/discover_form.html',context)


def deletediscover(request,pk):
    discov = Discover.objects.get(id=pk)
    if request.method == 'POST':
        discov.delete()
        return redirect('discovertable')
    context = {'obj': discov}
    return render(request,'disease/delete.html',context)
#####################################################################################################################



def duser(request,pk):
    user = Users.objects.get(email=pk)
    context = {'user': user}
    return render(request, 'user.html',context)

def dusers(request):
    users = Users.objects.all()
    context = {
        'users': users
    }
    return render(request,'disease/users.html',context)


def createdusers(request):
    form = UsersForm
    if request.method == 'POST':
        form = UsersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
    context = {'form': form}
    return render(request,'disease/users_form.html',context)



def updatedusers(request,pk):
    user = Users.objects.get(email=pk)
    form = UsersForm(instance=user)
    if request.method == 'POST':
        form = UsersForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            return redirect('users')
    context = {'form' : form}
    return render(request,'disease/users_form.html',context)


def deletedusers(request,pk):
    user = Users.objects.get(email=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('users')
    context = {'obj': user}
    return render(request,'disease/delete.html',context)

#####################################################################################################################

def publicservant(request,pk):
    publicservant = Publicservant.objects.get(email=pk)
    context = {'publicservant':publicservant}
    return render(request, 'publicservant.html',context)

def publicservants(request):
    publicservants = Publicservant.objects.all()
    context = {
        'publicservants': publicservants
    }
    return render(request,'disease/publicservants.html',context)


def createpublicservant(request):
    form = PublicServantForm
    if request.method == 'POST':
        form = PublicServantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('publicservants')
    context = {'form': form}
    return render(request,'disease/publicservant_form.html',context)



def updatepublicservant(request,pk):
    publicservant = Publicservant.objects.get(email=pk)
    form = PublicServantForm(instance=publicservant)
    if request.method == 'POST':
        form = PublicServantForm(request.POST,instance=publicservant)
        if form.is_valid():
            form.save()
            return redirect('publicservants')
    context = {'form' : form}
    return render(request,'disease/publicservant_form.html',context)


def deletepublicservant(request,pk):
    user = Publicservant.objects.get(email=pk)
    if request.method == 'POST':
        user.delete()
        return redirect('publicservants')
    context = {'obj': user}
    return render(request,'disease/delete.html',context)

#####################################################################################################################

def doctor(request,pk):
    doctor = Doctor.objects.get(email=pk)
    context = {'doctor':doctor}
    return render(request, 'doctor.html',context)

def doctors(request):
    doctors = Doctor.objects.all()
    context = {
        'doctors': doctors
    }
    return render(request,'disease/doctors.html',context)


def createdoctor(request):
    form = DoctorForm
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    context = {'form': form}
    return render(request,'disease/doctorform.html',context)



def updatedoctor(request,pk):
    doct = Doctor.objects.get(email=pk)
    form = DoctorForm(instance=doct)
    if request.method == 'POST':
        form = DoctorForm(request.POST,instance=doct)
        if form.is_valid():
            form.save()
            return redirect('doctors')
    context = {'form' : form}
    return render(request, 'disease/doctorform.html',context)


def deletedoctors(request,pk):
    doctor = Doctor.objects.get(email=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('doctors')
    context = {'obj': doctor}
    return render(request,'disease/delete.html',context)

#####################################################################################################################
def specialize(request,pk):
    specialize = Specialize.objects.get(id=pk)
    context = {'specialize': specialize}
    return render(request, 'specialize.html',context)

def specializes(request):
    specialize = Specialize.objects.all()
    context = {
        'specialize': specialize
    }
    return render(request,'disease/specializes.html',context)


def createspecialize(request):
    form = SpecializeForm
    if request.method == 'POST':
        form = SpecializeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('specializes')
    context = {'form': form}
    return render(request,'disease/specialize_form.html',context)



def updatespecialize(request,pk):
    specialize = Specialize.objects.get(id=pk)
    form = SpecializeForm(instance=specialize)
    if request.method == 'POST':
        form = SpecializeForm(request.POST,instance=specialize)
        if form.is_valid():
            form.save()
            return redirect('specializes')
    context = {'form' : form}
    return render(request,'disease/specialize_form.html',context)


def deletespecialize(request,pk):
    specialize = Specialize.objects.get(id=pk)
    if request.method == 'POST':
        specialize.delete()
        return redirect('specializes')
    context = {'obj': specialize}
    return render(request,'disease/delete.html',context)


#####################################################################################################################

def record(request,pk):
    record = Record.objects.get(id=pk)
    context = {'record':record}
    return render(request, 'record.html',context)

def records(request):
    records = Record.objects.all()
    context = {
        'records': records
    }
    return render(request,'disease/records.html',context)


def createrecords(request):
    form = RecordForm
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('records')
    context = {'form': form}
    return render(request,'disease/record_form.html',context)



def updaterecords(request,pk):
    #aname = Country.objects.get(cname=pk)
    #dis = Disease.objects.get(disease_code=pk)
    record = Record.objects.get(id=pk)#,cname=aname,disease_code=dis)
    form = RecordForm(instance=record)
    if request.method == 'POST':
        form = RecordForm(request.POST,instance=record)
        if form.is_valid():
            form.save()
            return redirect('records')
    context = {'form' : form}
    return render(request,'disease/record_form.html',context)


def deleterecord(request,pk):
    record = Record.objects.get(id=pk)
    if request.method == 'POST':
        record.delete()
        return redirect('records')
    context = {'obj': record}
    return render(request,'disease/delete.html',context)


