from rest_framework import serializers

from vet.models import PetOwner, Pet, PetDate, BranchOffice

# Serializers define the API representation.

###
class OwnersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = [
            "id",
            "first_name",
            "last_name",
        ]


class OwnersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetOwner
        fields = "__all__"


###
class PetsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "type",
        ]


class PetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = "__all__"


###
class DatesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = [
            "id",
            "type",
            "datetime",
        ]


class DatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetDate
        fields = "__all__"


###
class BranchOfficesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchOffice
        fields = [
            "id",
            "alias",
        ]


class BranchOfficesSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchOffice
        fields = "__all__"


###
class OwnerPetsSerializer(serializers.ModelSerializer):
    pets = PetsListSerializer(many=True)

    class Meta:
        model = PetOwner
        fields = [
            "id",
            "first_name",
            "last_name",
            "address",
            "email",
            "phone",
            "created_at",
            "pets",
        ]


class PetOwnerSerializer(serializers.ModelSerializer):
    owner = OwnersListSerializer()

    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "type",
            "owner",
        ]


class PetDatesSerializer(serializers.ModelSerializer):
    dates = DatesSerializer(many=True)

    class Meta:
        model = Pet
        fields = [
            "id",
            "name",
            "type",
            "dates",
        ]


class BranchOfficeDatesSerializer(serializers.ModelSerializer):
    office_dates = DatesListSerializer(many=True)

    class Meta:
        model = BranchOffice
        fields = [
            "id",
            "alias",
            "zip_code",
            "address",
            "phone",
            "longitude",
            "latitude",
            "created_at",
            "office_dates",
        ]


class OwnerPetsDatesSerializer(serializers.ModelSerializer):
    pets = PetDatesSerializer(many=True)

    class Meta:
        model = PetOwner
        fields = [
            "id",
            "first_name",
            "last_name",
            "address",
            "email",
            "phone",
            "created_at",
            "pets",
        ]


# from rest_framework import serializers

# from vet.models import PetOwner, Pet, PetDate

# # Serializers define the API representation.
# class OwnersSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PetOwner
#         fields = [
#             "id",
#             "first_name",
#             "last_name",
#             "email",
#             "phone",
#             "address",
#             "created_at",
#         ]


# class PetsSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Pet
#         fields = ["id", "name", "type"]


# class DatessSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = PetDate
#         fields = ["id", "datetime", "type", "created_at"]
