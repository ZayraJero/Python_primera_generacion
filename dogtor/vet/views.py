from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import View, TemplateView, DetailView

from .models import PetOwner, Pet


# Create your views here.

# Clase
class Test(View):
    def get(self, request):
        return HttpResponse("hello clase vista")


# Owners
class Owners(View):
    def get(self, request):
        owners = PetOwner.objects.all()
        context = {"owners": owners}

        template = loader.get_template("vet/owners/list.html")
        return HttpResponse(template.render(context, request))


class OwnersList(TemplateView):
    template_name = "vet/owners/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context, "Esto viene del padre, templateView")
        context["owners"] = PetOwner.objects.all()
        print(context, "esto le agregamos nosotros")
        return context


class OwnersDetail(DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"


# Pets
class PetsList(View):
    def get(self, request):
        pets = Pet.objects.all()
        context = {"pets": pets}

        template = loader.get_template("vet/pets/list.html")
        return HttpResponse(template.render(context, request))


class PetsDetail(TemplateView):
    template_name = "vet/pets/detail.html"

    def get_context_data(self, **kwargs):
        pk = self.kwargs.get("pk")
        context = super().get_context_data(**kwargs)
        context["pets"] = Pet.objects.get(pk=pk)
        return context


# def list_pet_owners(request):
#     """List owners."""
#     owners = PetOwner.objects.all()
#     context = {"owners": owners}

#     template = loader.get_template("vet/owners/list.html")
#     return HttpResponse(template.render(context, request))

# Vista como función
# def test(request):
#     print(request.__dict__)
#     return HttpResponse("hello")
