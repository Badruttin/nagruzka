from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import UchebniyPlan

class UPlanResource(resources.ModelResource):
    class Meta:
        model = UchebniyPlan
        import_id_fields = ['idd'] 
        skip_unchanged = True
        report_skipped = True
        fields = ('idd','number','number_2','u_plan','faculty','block','disciplina','cafedra','kurs_semestr','gruppa','students_count','weeks','vid_zanatiy','chasov','vid_control','individ_zanyatya','nagruz_auditor','nagruz_inoe','nagruz_inoe_char','nagruz_itogo','n_potok','id_first_group_potok','description')


         

@admin.register(UchebniyPlan)
class UchebniyPlanAdmin(ImportExportModelAdmin):
    resource_class = UPlanResource
    list_display = ['idd','number','number_2','u_plan','faculty','block','disciplina','cafedra','kurs_semestr','gruppa','students_count','weeks','vid_zanatiy','chasov','vid_control','individ_zanyatya','nagruz_auditor','nagruz_inoe','nagruz_inoe_char','nagruz_itogo','n_potok','id_first_group_potok','description']
    list_filter = ['faculty','cafedra']
    search_fields = ['faculty', 'disciplina']