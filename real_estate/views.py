# from django.http import Http404, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm, PropertyForm
from .models import Property
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm

# Signup view
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'real_estate/signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                if user.role == 'seller':
                    return redirect('seller_dashboard')
                else:
                    return redirect('buyer_dashboard')
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = AuthenticationForm()

    return render(request, 'real_estate/login.html', {'form': form})

# Seller dashboard
@login_required
def seller_dashboard(request):
    if request.user.role != 'seller':
        return redirect('home')  # Restrict non-sellers
    properties = Property.objects.filter(seller=request.user)
    return render(request, 'real_estate/seller_dashboard.html', {'properties': properties})

# Add property
@login_required
def add_property(request):
    if request.user.role != 'seller':
        return redirect('home')
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.seller = request.user
            property.save()
            return redirect('seller_dashboard')
    else:
        form = PropertyForm()
    return render(request, 'real_estate/add_property.html', {'form': form})

# Edit property
@login_required
def edit_property(request, property_id):
    property = get_object_or_404(Property, id=property_id, seller=request.user)
    if request.method == 'POST':
        form = PropertyForm(request.POST, instance=property)
        if form.is_valid():
            form.save()
            return redirect('seller_dashboard')
    else:
        form = PropertyForm(instance=property)
    return render(request, 'real_estate/edit_property.html', {'form': form})

# Delete property
@login_required
def delete_property(request, property_id):
    property = get_object_or_404(Property, id=property_id, seller=request.user)
    if request.method == 'POST':
        property.delete()
        return redirect('seller_dashboard')
    return render(request, 'real_estate/delete_property.html', {'property': property})

#property detail
@login_required
def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk, seller=request.user)
    return render(request, 'real_estate/property_detail.html', {'property': property})

#buyer dashboard
@login_required
def buyer_dashboard(request):
    if request.user.role != 'buyer':
        return redirect('home')  # Redirect if not a buyer
    properties = Property.objects.filter(available=True)  # Show only available properties
    return render(request, 'real_estate/buyer_dashboard.html', {'properties': properties})

#property detail buyer
@login_required
def property_detail_buyer(request, pk):
    property = get_object_or_404(Property, pk=pk, available=True)  # Ensure property is available
    return render(request, 'real_estate/property_detail_buyer.html', {'property': property})

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

#forgot_password
def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            return render(request, 'real_estate/password_reset_done.html')
    else:
        form = PasswordResetForm()

    return render(request, 'real_estate/forgot_password.html', {'form': form})