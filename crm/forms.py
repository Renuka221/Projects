from django import forms
from .models import Customer, CustomerMessage, ChurnFeature, ProductPurchase

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class MessageForm(forms.ModelForm):
    class Meta:
        model = CustomerMessage
        fields = '__all__'

class ChurnFeatureForm(forms.ModelForm):
    class Meta:
        model = ChurnFeature
        fields = '__all__'

class PurchaseForm(forms.ModelForm):
    class Meta:
        model = ProductPurchase
        fields = '__all__'
