from django.urls import reverse

from chargily_epay_django.models import AnonymPayment, FakePaymentMixin
from chargily_epay_django.utils import get_webhook_url

# Create your models here.


class Sponsor(FakePaymentMixin,AnonymPayment):
    webhook_url = "create-sponsor"
    
    fake_payment_url = "fake-sponsor"

    def generate_back_url(self):
        app_url = reverse(
            "sponsor-status", kwargs={"invoice_number": self.invoice_number}
        )
        return get_webhook_url(app_url)
