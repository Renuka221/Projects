from django.shortcuts import render, redirect
from .forms import CustomerForm, MessageForm, ChurnFeatureForm, PurchaseForm
from .models import Customer, ProductPurchase, CustomerMessage, ChurnFeature
from .forms import MessageForm
import joblib
import os
from django.conf import settings
import csv


def base(request):
    return render(request, 'crm/base.html')

tfidf = joblib.load(r"crm\ml_models\tfidf_vectorizer.pkl")
sentiment_model = joblib.load(r"crm\ml_models\sentiment_model.pkl")

def predict_sentiment(request):
    sentiment = ''
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['message_text']
            vector = tfidf.transform([text])
            pred = sentiment_model.predict(vector)[0]
            sentiment = pred
    else:
        form = MessageForm()
        
    return render(request, 'crm/predict_sentiment.html', {'form': form, 'sentiment': sentiment})

def dataset_view(request):
    dataset_path = os.path.join(settings.MEDIA_ROOT, 'ecommerce_datasets', 'customer_messages.csv')

    data = []

    try:
        with open(dataset_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        data = None

    return render(request, 'crm/dataset.html', {'data': data})


# Add Customer
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CustomerForm()
    return render(request, 'crm/add_customer.html', {'form': form})

# Add Message
def add_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = MessageForm()
    return render(request, 'crm/add_message.html', {'form': form})

# Add Churn Feature
def add_churn_feature(request):
    if request.method == 'POST':
        form = ChurnFeatureForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = ChurnFeatureForm()
    return render(request, 'crm/add_churn.html', {'form': form})

# Add Purchase
def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PurchaseForm()
    return render(request, 'crm/add_purchase.html', {'form': form})

# Generic success page
def success(request):
    return render(request, 'crm/success.html')


def view_customers(request):
    customers = Customer.objects.all()
    return render(request, 'crm/view_customers.html', {'customers': customers})

def view_messages(request):
    messages = CustomerMessage.objects.all()
    return render(request, 'crm/view_messages.html', {'messages': messages})

def view_purchases(request):
    purchases = ProductPurchase.objects.all()
    return render(request, 'crm/view_purchases.html', {'purchases': purchases})

def view_churn_features(request):
    churn_data = ChurnFeature.objects.all()
    return render(request, 'crm/view_churn.html', {'churn_data': churn_data})


import pandas as pd
from django.shortcuts import render
from django.conf import settings
import os

def customer_dashboard(request):

    result = None

    if request.method == "POST":
        customer_name = request.POST.get('customer_name')
        recommended_offer = request.POST.get('recommended_offer')
        purchase_probability = float(request.POST.get('purchase_probability'))

        # Load Dataset
        path = os.path.join(r'media\ecommerce_datasets\customer_data.csv')
        df = pd.read_csv(path)

        # Simple Prediction Logic
        if purchase_probability >= 70:
            customer_type = "Loyal Customer"
            next_product = "Premium Membership"
            risk = "Low"
            category = "Electronics"
            # Customer Behavior Prediction
            will_purchase_next = f"YES ({purchase_probability}%)"
            chance_of_leaving = f"{100 - purchase_probability}%"
            engagement_level = "High"
            best_time_offer = "Evening 7PM – 10PM"

        elif purchase_probability >= 40:
            customer_type = "Regular Customer"
            next_product = "Discounted Bundle"
            risk = "Medium"
            category = "Fashion"
            # Customer Behavior Prediction
            will_purchase_next = f"YES ({purchase_probability}%)"
            chance_of_leaving = f"{100 - purchase_probability}%"
            engagement_level = "Medium"
            best_time_offer = "Afternoon 2PM – 5PM"

        else:
            customer_type = "At Risk Customer"
            next_product = "Re-engagement Offer"
            risk = "High"
            category = "Groceries"
            # Customer Behavior Prediction
            will_purchase_next = f"NO ({purchase_probability}%)"
            chance_of_leaving = f"{100 - purchase_probability}%"
            engagement_level = "Low"
            best_time_offer = "Morning 10AM – 12PM"

        # Combine everything in result
        result = {
            "customer_name": customer_name,
            "customer_type": customer_type,
            "purchase_probability": purchase_probability,
            "next_product": next_product,
            "recommended_offer": recommended_offer,
            "risk": risk,
            "category": category,
            "will_purchase_next": will_purchase_next,
            "chance_of_leaving": chance_of_leaving,
            "engagement_level": engagement_level,
            "best_time_offer": best_time_offer
        }

    return render(request, "crm/customer_dashboard.html", {"result": result})
