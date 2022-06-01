from django.urls import path
from django.conf import settings

from sponsor.views import (
    CreateSponsor,
    SponsorStatus,
    ConfirmSponsor,
    FakeSponsor,
)


urlpatterns = [
    path("confirm-sponsor/", ConfirmSponsor.as_view(), name="confirm-sponsor"),
    path("", CreateSponsor.as_view(), name="create-sponsor"),
    path(
        "sponsor-status/<slug:invoice_number>/",
        SponsorStatus.as_view(),
        name="sponsor-status",
    ),
]

if settings.DEBUG: 
    urlpatterns = urlpatterns + [
        path(
            "fake-sponsor/<slug:invoice_number>/",
            FakeSponsor.as_view(),
            name="fake-sponsor",
        ),

    ]