from django.shortcuts import render

# Create your views here.
from chargily_epay_django.views import (
    CreatePaymentView,
    FakePaymentView,
    PaymentConfirmationView,
    PaymentObjectDoneView,
)

from sponsor.forms import SponsorForm
from sponsor.models import Sponsor


class CreateSponsor(CreatePaymentView):
    payment_create_faild_url = ""
    template_name: str = "sponsor/sponsor.html"
    form_class = SponsorForm


class SponsorStatus(PaymentObjectDoneView):
    model = Sponsor
    template_name: str = "sponsor/sponsor-status.html"


class ConfirmSponsor(PaymentConfirmationView):
    model = Sponsor


class FakeSponsor(FakePaymentView):
    model = Sponsor
