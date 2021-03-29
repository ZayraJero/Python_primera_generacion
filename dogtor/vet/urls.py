from django.urls import path

from .views import (
    OwnersList,
    OwnersDetail,
    OwnersCreate,
    OwnersUpdate,
    PetsList,
    PetsDetail,
    PetsCreate,
    PetsUpdate,
)

urlpatterns = [
    path("owners/", OwnersList.as_view(), name="owners_list"),
    path("owners/add/", OwnersCreate.as_view(), name="owners_create"),
    path("owners/<int:pk>/", OwnersDetail.as_view(), name="owners_detail"),
    path("owners/<int:pk>/update/", OwnersUpdate.as_view(), name="owners_update"),
    path("pets/", PetsList.as_view(), name="pets_list"),
    path("pets/add/", PetsCreate.as_view(), name="pets_create"),
    path("pets/<int:pk>/", PetsDetail.as_view(), name="pets_detail"),
    path("pets/<int:pk>/update/", PetsUpdate.as_view(), name="pets_update"),
]
# SIN INCLUDE
# path("pets/", PetsList.as_view()),
# path("pets/<int:pk>/", PetsDetail.as_view()),
# path("test/", Test.as_view()),
