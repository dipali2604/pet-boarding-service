
from django import forms
from app.models import Complaint, Payment, Review,Pet,Profile,Boarding


class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ('subject','detail')

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating','review')

class PetForm(forms.ModelForm):       
    class Meta:       
        model = Pet       
        fields = ('name','pettype','age','description','specialinstruction','photo')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('firstname','lastname','email','phone','gender','dob','photo','altcontact','address','city','pincode')
        widgets = {
            'dob': forms.DateInput(attrs={'class': 'datepicker', 'id': 'data_input','type':'date'})
        }
class BoardingForm(forms.ModelForm):
    class Meta:       
        model = Boarding       
        fields = ("duration","pet",'pick_date')
        widgets = {
            'duration': forms.NumberInput(attrs={'class': 'days', 'id': 'day_input','type':'number'}),
            'pick_date': forms.DateInput(attrs={'class': 'pick_date', 'id': 'pick_date','type':'date'})
        }

class PaymentForm(forms.ModelForm):       
    class Meta:       
        model = Payment       
        fields = ('payment_method',)       