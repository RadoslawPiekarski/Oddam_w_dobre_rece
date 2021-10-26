from django.shortcuts import render
from django.views import View
from django.db.models import Sum
from .models import Donation, Institution


# Create your views here.
class LandingPage(View):
    def get(self, request):
        all_given_donations = list(Donation.objects.aggregate(Sum('quantity')).values())[0]
        all_donated_organisations = Donation.objects.values('institution').count()
        sample_foundations = Institution.objects.filter(type='F')[:3]
        sample_organizations = Institution.objects.filter(type='O')[:3]
        sample_collections = Institution.objects.filter(type='Z')[:3]
        return render(request, "oddam_app/index.html", {
            "all_given_donations": all_given_donations,
            "all_donated_organisations": all_donated_organisations,
            "sample_foundations": sample_foundations,
        })


class AddDonation(View):
    def get(self, request):
        return render(request, "oddam_app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "oddam_app/login.html")


class Register(View):
    def get(self, request):
        return render(request, "oddam_app/register.html")
