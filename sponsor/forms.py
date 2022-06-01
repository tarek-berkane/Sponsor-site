from dataclasses import field
from django.forms import Form, ModelForm, ValidationError

from sponsor.models import Sponsor


class SponsorForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(SponsorForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs["class"] = "form-control mb-3"
            if field_name == "comment":
                field.widget.attrs["rows"] = 5

    class Meta:
        model = Sponsor
        fields = ["client", "client_email", "amount", "mode", "comment"]


    def clean_amount(self):
        amount = self.cleaned_data['amount']

        if amount < 200:
            raise ValidationError('amount of sponsor must be bigger than 200DA')
        
        return amount