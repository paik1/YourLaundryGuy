from django import forms
from .models import OrderInfo
import datetime

class DateInput(forms.DateInput):
    input_type = 'date'

class UserForm(forms.ModelForm):

    def present_or_future_date(value):
        if value < datetime.date.today():
            raise forms.ValidationError("The date cannot be in the past!")
        return value

    order_date = forms.DateField(widget=DateInput,validators=[present_or_future_date])

    class Meta:
        model = OrderInfo
        fields = ('phone_number','categories','time_slot','order_date', 'express_d')