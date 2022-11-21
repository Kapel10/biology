from django.db import models


# Create your models here.
class Diseasetype(models.Model):
    id = models.IntegerField(primary_key=True)
    description = models.CharField(max_length=140, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'diseasetype'

    def __str__(self):
        return str(self.id)



class Country(models.Model):
    cname = models.CharField(primary_key=True, max_length=50)
    population = models.BigIntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'country'

    def __str__(self):
        return str(self.cname)



class Disease(models.Model):
    disease_code = models.CharField(primary_key=True, max_length=50)
    pathogen = models.CharField(max_length=20, blank=True, null=True)
    description = models.CharField(max_length=140, blank=True, null=True)
    id = models.ForeignKey('Diseasetype', models.DO_NOTHING, db_column='id', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'
    def __str__(self):
        return str(self.disease_code)


class Discover(models.Model):
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')
    disease_code = models.ForeignKey('Disease', models.DO_NOTHING, db_column='disease_code')
    first_enc_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'discover'
        constraints = [
            models.UniqueConstraint(fields=['cname', 'disease_code'], name='discover_link')
        ]

    def __str__(self):
        return str(self.cname)

class Users(models.Model):
    email = models.CharField(primary_key=True, max_length=60)
    name = models.CharField(max_length=30, blank=True, null=True)
    surname = models.CharField(max_length=40, blank=True, null=True)
    salary = models.IntegerField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
    def __str__(self):
        return str(self.email)


class Publicservant(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)
    department = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'publicServant'
    def __str__(self):
        return str(self.email)



class Doctor(models.Model):
    email = models.OneToOneField('Users', models.DO_NOTHING, db_column='email', primary_key=True)

    degree = [
        ('Bachelor', 'Bachelor'),
        ('MD', 'MD'),
        ('PhD', 'PhD'),
        ('Doctoral', 'Doctoral'),

    ]

    degree = models.CharField(max_length=100, choices=degree, default='Bachelor')

    class Meta:
        managed = False
        db_table = 'doctor'

    def __str__(self):
        return str(self.email)


class Specialize(models.Model):
    sid = models.ForeignKey(Diseasetype, models.DO_NOTHING, db_column='sid')
    email = models.ForeignKey(Doctor, models.DO_NOTHING, db_column='email')

    class Meta:
        managed = False
        db_table = 'specialize'
        #unique_together = (('id', 'email'),)
        constraints = [
             models.UniqueConstraint(fields=['sid', 'email'], name='specialize_link')
        ]

    def __str__(self):
        return str(self.email)

class Record(models.Model):
    email = models.ForeignKey(Publicservant, models.DO_NOTHING, db_column='email')
    cname = models.ForeignKey(Country, models.DO_NOTHING, db_column='cname')
    disease_code = models.ForeignKey(Disease, models.DO_NOTHING, db_column='disease_code')
    total_deaths = models.IntegerField(blank=True, null=True)
    total_patients = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'record'
        unique_together = (('email', 'cname', 'disease_code'),)
        constraints = [
           models.UniqueConstraint(fields=['email', 'cname','disease_code'], name='record-link')
        ]

    def __str__(self):
        return str(self.email)
