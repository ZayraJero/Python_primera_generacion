from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.urls import reverse_lazy

from .models import PetOwner, Pet
from .forms import OwnerForm

# Create your views here.
class OwnersList(LoginRequiredMixin, ListView):
    model = PetOwner
    template_name = "vet/owners/list.html"
    context_object_name = "owners"
    login_url = reverse_lazy("login")


class OwnersDetail(LoginRequiredMixin, DetailView):
    model = PetOwner
    template_name = "vet/owners/detail.html"
    context_object_name = "owner"
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(context["view"].__dict__)
        return context


class OwnersCreate(LoginRequiredMixin, CreateView):
    model = PetOwner
    template_name = "vet/owners/create.html"
    form_class = OwnerForm
    success_url = reverse_lazy("vet:owners_list")
    login_url = reverse_lazy("login")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["owners"] = PetOwner.objects.all().order_by("created_at")

        return context


class OwnersUpdate(LoginRequiredMixin, UpdateView):
    model = PetOwner
    form_class = OwnerForm
    template_name = "vet/owners/update.html"
    success_url = reverse_lazy("vet:owners_list")
    login_url = reverse_lazy("login")


class PetsList(LoginRequiredMixin, ListView):
    model = Pet
    template_name = "vet/pets/list.html"
    context_object_name = "pets"
    login_url = reverse_lazy("login")


class PetsDetail(LoginRequiredMixin, DetailView):
    model = Pet
    template_name = "vet/pets/detail.html"
    context_object_name = "pet"
    login_url = reverse_lazy("login")


class PetsCreate(LoginRequiredMixin, CreateView):
    model = Pet
    template_name = "vet/pets/create.html"
    fields = ["name", "type", "owner"]
    success_url = reverse_lazy("vet:pets_list")
    login_url = reverse_lazy("login")

    def get_initial(self):
        initial = {}
        for queryparam in self.request.GET:
            initial[queryparam] = self.request.GET[queryparam]

        return initial


# class PetsCreate(CreateView):
#     model = Pet
#     template_name = "vet/pets/create.html"
#     form_class = PetForm
#     success_url = reverse_lazy("vet:pets_list")


class PetsUpdate(UpdateView):
    model = Pet
    template_name = "vet/pets/update.html"
    fields = ["name", "type", "owner"]
    success_url = reverse_lazy("vet:pets_list")


# Clase
# class Test(View):
#     def get(self, request):
#         return HttpResponse("hello clase vista")


# Owners
# class Owners(View):
#     def get(self, request):
#         owners = PetOwner.objects.all()
#         context = {"owners": owners}

#         template = loader.get_template("vet/owners/list.html")
#         return HttpResponse(template.render(context, request))


# class OwnersList(TemplateView):
#     template_name = "vet/owners/list.html"

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         print(context, "Esto viene del padre, templateView")
#         context["owners"] = PetOwner.objects.all()
#         print(context, "esto le agregamos nosotros")
#         return context


# Pets
# class PetsList(View):
#     def get(self, request):
#         pets = Pet.objects.all()
#         context = {"pets": pets}

#         template = loader.get_template("vet/pets/list.html")
#         return HttpResponse(template.render(context, request))


# class PetsDetail(TemplateView):
#     template_name = "vet/pets/detail.html"

#     def get_context_data(self, **kwargs):
#         pk = self.kwargs.get("pk")
#         context = super().get_context_data(**kwargs)
#         context["pets"] = Pet.objects.get(pk=pk)
#         return context


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
