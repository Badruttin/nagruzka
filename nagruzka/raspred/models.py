from django.db import models
from django.utils import timezone

class UchebniyPlan(models.Model):
    idd = models.IntegerField(null=True)
    number = models.IntegerField(null=True)
    number_2 = models.IntegerField(null=True)
    u_plan = models.CharField(max_length=200) #09.03.03 ПИ(ЭиУ)22.plx
    faculty = models.CharField(max_length=200) #ФИИТ
    block = models.CharField(max_length=200) #Б1.В.ДВ.01.01
    disciplina = models.CharField(max_length=200) #1C-Аналитика
    cafedra = models.CharField(max_length=200) #67-ПИ
    kurs_semestr = models.CharField(max_length=200) #4/8
    gruppa = models.CharField(max_length=200) #ПИ(ЭиУ)-41
    students_count = models.IntegerField(null=True)
    weeks = models.IntegerField(null=True)
    vid_zanatiy = models.CharField(max_length=200) #Лек
    chasov = models.IntegerField(null=True)
    vid_control = models.CharField(max_length=200) #Эк
    individ_zanyatya = models.IntegerField(null=True)
    nagruz_auditor = models.IntegerField(null=True)
    nagruz_inoe = models.IntegerField(null=True)
    nagruz_inoe_char = models.CharField(max_length=200, default='')
    nagruz_itogo = models.IntegerField(null=True)
    n_potok = models.IntegerField(null=True)
    id_first_group_potok = models.IntegerField(null=True)
    description = models.TextField(null=True)
    import_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['idd']
        indexes = [
            models.Index(fields=['disciplina']),
        ]

    def __str__(self):
        return self.disciplina

class Desciplina(models.Model):
    disciplina_id = models.IntegerField(primary_key=True)
    disciplina_block = models.CharField(max_length=30)
    faculty_short_name = models.CharField(max_length=10)
    cafedra_short_name = models.CharField(max_length=20)
    disciplina_name = models.CharField(max_length=250)
    disciplina_description = models.TextField()
    import_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)


class Faculty(models.Model):
    faculty_id = models.IntegerField(primary_key=True)    
    faculty_short_name = models.CharField(max_length=10)
    faculty_full_name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    #TODO cafedras 

class Cafedra(models.Model):
    cafedra_id = models.IntegerField(primary_key=True)
    cafedra_short_name = models.CharField(max_length=20)
    cafedra_full_name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    #TODO Faculty