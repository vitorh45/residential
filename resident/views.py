from django.shortcuts import render, redirect, get_object_or_404
from .forms import ResidentCreationForm, ResidentEditForm, HouseResidentnFormset, VehicleResidentnFormset
from django.contrib.auth.decorators import login_required
from .models import Resident
from django.contrib.auth import authenticate, login as auth_login


def register(request):

    form = ResidentCreationForm(request.POST or None)
    if form.is_valid():
        form.save()
        user = authenticate(request, username=form.cleaned_data['cpf'], password=form.cleaned_data['password1'])
        auth_login(request, user)
        return redirect('edit')

    return render(request, 'resident/register.html', {
        'form': form
    })


def edit(request):

    form = ResidentEditForm(request.POST or None, instance=request.user)
    house_formset = HouseResidentnFormset(request.POST or None, instance=request.user)
    vehicle_formset = VehicleResidentnFormset(request.POST or None, instance=request.user)
    if form.is_valid() and house_formset.is_valid() and vehicle_formset.is_valid():
        form.save()
        house_formset.save()
        vehicle_formset.save()
        return redirect('edit')

    return render(request, 'resident/edit.html', {
        'form': form,
        'houses': house_formset,
        'vehicles': vehicle_formset
    })


@login_required
def detail(request):
    resident = get_object_or_404(Resident, cpf=request.user.cpf)
    return render(request, 'resident/detail.html', {
        'resident': resident
    })