from django.urls import path, include
from .views import (
    ListOwnersAPIView,
    CreateOwnersAPIView,
    RetrieveOwnersAPIView,
    UpdateOwnersAPIView,
    DestroyOwnersAPIView,
    ListPetsAPIView,
    CreatePetsAPIView,
    RetrievePetsAPIView,
    UpdatePetsAPIView,
    DestroyPetsAPIView,
    ListDatesAPIView,
    CreateDatesAPIView,
    RetrieveDatesAPIView,
    UpdateDatesAPIView,
    DestroyDatesAPIView,
    ListBranchOfficesAPIView,
    CreateBranchOfficesAPIView,
    RetrieveBranchOfficesAPIView,
    UpdateBranchOfficesAPIView,
    DestroyBranchOfficesAPIView,
    RetrieveOwnerPetsAPIView,
    RetrievePetOwnerAPIView,
    RetrievePetDatesAPIView,
    RetrieveBranchOfficesDatesAPIView,
    RetrieveOwnerPetsDatesAPIView,
)


urlpatterns = [
    path("owners/", ListOwnersAPIView.as_view(), name="list-owners"),
    path("owners/create/", CreateOwnersAPIView.as_view(), name="create-owners"),
    path("owners/<int:pk>/", RetrieveOwnersAPIView.as_view(), name="retrieve-owners"),
    path(
        "owners/<int:pk>/update/", UpdateOwnersAPIView.as_view(), name="update-owners"
    ),
    path(
        "owners/<int:pk>/destroy/",
        DestroyOwnersAPIView.as_view(),
        name="destroy-owners",
    ),
    path("pets/", ListPetsAPIView.as_view(), name="list-pets"),
    path("pets/create/", CreatePetsAPIView.as_view(), name="create-pets"),
    path("pets/<int:pk>/", RetrievePetsAPIView.as_view(), name="retrieve-pets"),
    path("pets/<int:pk>/update/", UpdatePetsAPIView.as_view(), name="update-pets"),
    path("pets/<int:pk>/destroy/", DestroyPetsAPIView.as_view(), name="destroy-pets"),
    path("dates/", ListDatesAPIView.as_view(), name="list-dates"),
    path("dates/create/", CreateDatesAPIView.as_view(), name="create-dates"),
    path("dates/<int:pk>/", RetrieveDatesAPIView.as_view(), name="retrieve-dates"),
    path("dates/<int:pk>/update/", UpdateDatesAPIView.as_view(), name="update-dates"),
    path(
        "dates/<int:pk>/destroy/", DestroyDatesAPIView.as_view(), name="destroy-dates"
    ),
    path("branches/", ListBranchOfficesAPIView.as_view(), name="list-branchoffices"),
    path(
        "branches/create/",
        CreateBranchOfficesAPIView.as_view(),
        name="create-branchoffices",
    ),
    path(
        "branches/<int:pk>/",
        RetrieveBranchOfficesAPIView.as_view(),
        name="retrieve-branchoffices",
    ),
    path(
        "branches/<int:pk>/update/",
        UpdateBranchOfficesAPIView.as_view(),
        name="update-branchoffices",
    ),
    path(
        "branches/<int:pk>/destroy/",
        DestroyBranchOfficesAPIView.as_view(),
        name="destroy-branchoffices",
    ),
    path(
        "owners/<int:pk>/pets/",
        RetrieveOwnerPetsAPIView.as_view(),
        name="retrieve-owner-pets",
    ),
    path(
        "pets/<int:pk>/owner/",
        RetrievePetOwnerAPIView.as_view(),
        name="retrieve-pet-owner",
    ),
    path(
        "pets/<int:pk>/dates/",
        RetrievePetDatesAPIView.as_view(),
        name="retrieve-pet-dates",
    ),
    path(
        "branches/<int:pk>/dates/",
        RetrieveBranchOfficesDatesAPIView.as_view(),
        name="retrieve-branchoffice-dates",
    ),
    path(
        "owners/<int:pk>/pets/dates/",
        RetrieveOwnerPetsDatesAPIView.as_view(),
        name="retrieve-owner-pets-dates",
    ),
]


# from django.urls import path, include
# from rest_framework import routers
# from .views import OwnersViewSet, PetsViewSet, DatesViewSet

# router = routers.DefaultRouter()
# router.register(r"owners", OwnersViewSet)
# router.register(r"pets", PetsViewSet)
# router.register(r"dates", DatesViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]