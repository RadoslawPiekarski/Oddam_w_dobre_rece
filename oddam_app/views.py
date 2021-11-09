from django.shortcuts import render
from django.views import View
from django.db.models import Sum
from .models import Donation, Institution
from django.contrib.auth.models import User
from .forms import CreateUserForm, LoginForm
from django.contrib.auth import login
from django.contrib import messages


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
            "sample_organisations": sample_organizations,
            "sample_collections": sample_collections
        })


class AddDonation(View):
    def get(self, request):
        return render(request, "oddam_app/form.html")


class Login(View):
    def get(self, request):
        return render(request, "oddam_app/login.html")

    def post(self, request):
        form = LoginForm(request.POST);
        if form.is_valid():
            pass
            # TODO dokonczyc logowanie


class Register(View):
    def get(self, request):
        form = CreateUserForm()
        return render(request, "oddam_app/register.html", {
            "form": form
        })

# TODO add hash password or custom user view!!!
    def post(self, request):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = User(
                username=form.cleaned_data["email"],
                password=form.cleaned_data["password"],
                first_name=form.cleaned_data["firstname"],
                last_name=form.cleaned_data["lastname"],
                email=form.cleaned_data["email"],
            )
            user.save()
            return render(request, "oddam_app/index.html")
        messages.error(request, "Nie zarejestrowano użytkownika. Brak wymaganych danych")
        return render(request, "oddam_app/register.html", {"register_form": form})


    #     form = NewUserForm()
    #     return render(request, "oddam_app/register.html", {"register_form": form})
    #
    # def post(self, request):
    #     form = NewUserForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         login(request, user)
    #         messages.success(request, "Rejestracja zakończona sukcesem.")
    #         return render(request, "oddam_app/index.html")
    #     messages.error(request, "Nie zarejestrowano użytkownika. Brak wymaganych danych")
    #     return render(request, "oddam_app/register.html", {"register_form": form})
