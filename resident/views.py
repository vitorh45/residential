from django.shortcuts import render
from .forms import ResidentForm


def create(request):

    form = ResidentForm()

    return render(request, 'resident/register.html', {
        'form': form
    })
