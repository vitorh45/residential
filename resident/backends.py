from django.contrib.auth.backends import ModelBackend
from .models import Resident
from django.shortcuts import get_object_or_404


class EmailAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            print (username)
            user = Resident.objects.get(cpf=username)
            if user.check_password(password):
                return user
        except Resident.DoesNotExist:
            return None