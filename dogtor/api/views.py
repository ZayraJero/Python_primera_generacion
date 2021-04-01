from rest_framework import generics, filters, permissions

from django.contrib.auth.models import User

from vet.models import PetOwner, Pet, PetDate, BranchOffice

from .serializers import (
    BranchOfficesListSerializer,
    BranchOfficesSerializer,
    OwnersListSerializer,
    OwnersSerializer,
    PetsListSerializer,
    PetsSerializer,
    DatesListSerializer,
    DatesSerializer,
    OwnerPetsSerializer,
    PetOwnerSerializer,
    PetDatesSerializer,
    BranchOfficeDatesSerializer,
    OwnerPetsDatesSerializer,
    #
    UsersSerializer,
)

# # Create your views here.


# OWNER
class ListOwnersAPIView(generics.ListAPIView):
    queryset = PetOwner.objects.all().order_by("created_at")
    serializer_class = OwnersListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ["first_name", "last_name"]
    # permission_classes = [permissions.IsAdminUser]


class CreateOwnersAPIView(generics.CreateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer


class RetrieveOwnersAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer


class UpdateOwnersAPIView(generics.UpdateAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer


class DestroyOwnersAPIView(generics.DestroyAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnersSerializer


# PET
class ListPetsAPIView(generics.ListAPIView):
    queryset = Pet.objects.all().order_by("type")
    serializer_class = PetsListSerializer
    filterset_fields = ["name"]


class CreatePetsAPIView(generics.CreateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


class RetrievePetsAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


class UpdatePetsAPIView(generics.UpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


class DestroyPetsAPIView(generics.DestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


# DATE
class ListDatesAPIView(generics.ListAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesListSerializer


class CreateDatesAPIView(generics.CreateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer


class RetrieveDatesAPIView(generics.RetrieveAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer


class UpdateDatesAPIView(generics.UpdateAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer


class DestroyDatesAPIView(generics.DestroyAPIView):
    queryset = PetDate.objects.all()
    serializer_class = DatesSerializer


# BRANCH OFFICE
class ListBranchOfficesAPIView(generics.ListAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficesListSerializer


class CreateBranchOfficesAPIView(generics.CreateAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficesSerializer


class RetrieveBranchOfficesAPIView(generics.RetrieveAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficesSerializer


class UpdateBranchOfficesAPIView(generics.UpdateAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficesSerializer


class DestroyBranchOfficesAPIView(generics.DestroyAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficesSerializer


# RETRIEVE
class RetrieveOwnerPetsAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnerPetsSerializer


class RetrievePetOwnerAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetOwnerSerializer


class RetrievePetDatesAPIView(generics.RetrieveAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetDatesSerializer


class RetrieveBranchOfficesDatesAPIView(generics.RetrieveAPIView):
    queryset = BranchOffice.objects.all()
    serializer_class = BranchOfficeDatesSerializer


class RetrieveOwnerPetsDatesAPIView(generics.RetrieveAPIView):
    queryset = PetOwner.objects.all()
    serializer_class = OwnerPetsDatesSerializer


### GENERIC VIEWS CONJUNTAS, PERMITE MAS METODOS
class RetrieveUpdatePetsAPIView(generics.RetrieveUpdateAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetsSerializer


# USER
from rest_framework import permissions


class CreateUsersAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = []


#     VIEWSET
# from rest_framework import viewsets

# from vet.models import PetOwner, Pet, PetDate
# from .serializers import OwnersSerializer, PetsSerializer, DatesSerializer

# # Create your views here.
# class OwnersViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet del modelo PetOwners.
#     """

#     queryset = PetOwner.objects.all()
#     serializer_class = OwnersSerializer


# class PetsViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet del modelo Pet.
#     """

#     queryset = Pet.objects.all().order_by("created_at")
#     serializer_class = PetsSerializer


# class DatesViewSet(viewsets.ModelViewSet):
#     """
#     ViewSet del modelo PetDates.
#     """

#     queryset = PetDate.objects.all().order_by("created_at")
#     serializer_class = DatesSerializer