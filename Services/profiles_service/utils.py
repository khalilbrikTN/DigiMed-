
# BY : MOHAMED KHALIL BRK

# profiles/utils.py
from .models import Doctor, Patient
from django.db.models import Q

def search_doctors(specialty=None, sub_specialty=None, location=None):

    filters = Q()

    if specialty:
        filters &= Q(specialty__icontains=specialty)
    if sub_specialty:
        filters &= Q(sub_specialty__icontains=sub_specialty)
    if location:
        filters &= Q(worksin__location__icontains=location)  


    return Doctor.objects.filter(filters).distinct()


def search_patients(city=None, blood_type=None, age=None, gender=None):

    filters = Q()

    if city:
        filters &= Q(city__icontains=city)
    if blood_type:
        filters &= Q(blood_type__iexact=blood_type)
    if age:
        filters &= Q(age=age)
    if gender:
        filters &= Q(gender__iexact=gender)

    return Patient.objects.filter(filters).distinct()
