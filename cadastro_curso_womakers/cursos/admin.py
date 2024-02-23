from django.contrib import admin
from cursos.models import Curso

# Register your models here.
@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'nivel', 'carga_horaria']
    search_fields = ['titulo', 'nivel']
    list_filter = ['data_do_curso']
