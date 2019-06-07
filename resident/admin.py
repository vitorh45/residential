from django.contrib import admin
from .models import Resident, HouseResident, VehicleResident
from django_object_actions import DjangoObjectActions
from django.contrib import admin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


class HouseResidentInline(admin.TabularInline):
    model = HouseResident
    extra = 2


class VehicleResidentInline(admin.TabularInline):
    model = VehicleResident
    extra = 2


@admin.register(Resident)
class ResidentAdmin(DjangoObjectActions, admin.ModelAdmin):
    list_display = ('username', 'email', 'lot_block', 'cpf',)
    inlines = [
        HouseResidentInline,
        VehicleResidentInline
    ]

    def generate_pdf(self, request, obj):

        html_string = render_to_string('resident/resident_data.html', {'obj': obj})

        html = HTML(string=html_string)
        html.write_pdf(target='/tmp/{}.pdf'.format(obj.cpf))

        fs = FileSystemStorage('/tmp')
        with fs.open('{}.pdf'.format(obj.cpf)) as pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(obj.cpf)
            return response

    generate_pdf.label = 'Gerar PDF'
    generate_pdf.short_description = 'Clique para gerar o PDF com os dados da pessoa'

    change_actions = ('generate_pdf',)