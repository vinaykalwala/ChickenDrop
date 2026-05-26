from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.shortcuts import render


def home(request):

    offers = Offer.objects.filter(
        is_active=True
    )[:6]

    latest_updates = LatestUpdate.objects.filter(
        is_active=True
    )[:6]

    context = {

        'offers': offers,

        'latest_updates': latest_updates,
    }

    return render(
        request,
        'home.html',
        context
    )


def about(request):
    return render(request, 'about.html')


def terms_conditions(request):
    return render(request, 'terms.html')


def privacy_policy(request):
    return render(request, 'privacy.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)

            messages.success(
                request,
                "Login successful."
            )

            return redirect('dashboard')

        else:
            messages.error(
                request,
                "Invalid username or password."
            )

    return render(request, 'auth/login.html')


@login_required(login_url='login')
def logout_view(request):
    logout(request)

    messages.success(
        request,
        "Logged out successfully."
    )

    return redirect('login')


@login_required(login_url='login')
def dashboard(request):
    total_enquiries = ContactEnquiry.objects.count()

    new_enquiries = ContactEnquiry.objects.filter(
        status='new'
    ).count()

    read_enquiries = ContactEnquiry.objects.filter(
        status='read'
    ).count()

    context = {
        'total_enquiries': total_enquiries,
        'new_enquiries': new_enquiries,
        'read_enquiries': read_enquiries,
    }

    return render(
        request,
        'admin_panel/dashboard.html',
        context
    )

def contact_us(request):
    form = ContactEnquiryForm()

    if request.method == 'POST':
        form = ContactEnquiryForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your enquiry has been submitted successfully."
            )

            return redirect('contact_us')

    return render(request, 'contact/contact.html', {'form': form})


@login_required
def enquiry_dashboard(request):
    context = {
        'total_enquiries': ContactEnquiry.objects.count(),
        'new_enquiries': ContactEnquiry.objects.filter(status='new').count(),
        'read_enquiries': ContactEnquiry.objects.filter(status='read').count(),
    }

    return render(request, 'admin_panel/enquiry_dashboard.html', context)


@login_required
def enquiry_list(request):
    enquiries = ContactEnquiry.objects.all()

    return render(
        request,
        'admin_panel/enquiry_list.html',
        {'enquiries': enquiries}
    )


@login_required
def enquiry_detail(request, pk):
    enquiry = get_object_or_404(ContactEnquiry, pk=pk)

    if enquiry.status == 'new':
        enquiry.status = 'read'
        enquiry.save()

    return render(
        request,
        'admin_panel/enquiry_detail.html',
        {'enquiry': enquiry}
    )


@login_required
def enquiry_update(request, pk):
    enquiry = get_object_or_404(ContactEnquiry, pk=pk)

    form = ContactEnquiryUpdateForm(instance=enquiry)

    if request.method == 'POST':
        form = ContactEnquiryUpdateForm(
            request.POST,
            instance=enquiry
        )

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Enquiry updated successfully."
            )

            return redirect('enquiry_list')

    return render(
        request,
        'admin_panel/enquiry_update.html',
        {
            'form': form,
            'enquiry': enquiry
        }
    )


@login_required
def enquiry_delete(request, pk):
    enquiry = get_object_or_404(ContactEnquiry, pk=pk)
    enquiry.delete()

    messages.success(
        request,
        "Enquiry deleted successfully."
    )

    return redirect('enquiry_list')
@login_required
def offer_list(request):

    offers = Offer.objects.all()

    return render(
        request,
        'offers/offer_list.html',
        {'offers': offers}
    )


@login_required
def offer_create(request):

    form = OfferForm()

    if request.method == 'POST':

        form = OfferForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Offer created successfully.'
            )

            return redirect('offer_list')

    return render(
        request,
        'offers/offer_create.html',
        {'form': form}
    )


@login_required
def offer_update(request, pk):

    offer = get_object_or_404(
        Offer,
        pk=pk
    )

    form = OfferForm(
        instance=offer
    )

    if request.method == 'POST':

        form = OfferForm(
            request.POST,
            request.FILES,
            instance=offer
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Offer updated successfully.'
            )

            return redirect('offer_list')

    return render(
        request,
        'offers/offer_update.html',
        {
            'form': form,
            'offer': offer
        }
    )


@login_required
def offer_delete(request, pk):

    offer = get_object_or_404(
        Offer,
        pk=pk
    )

    if request.method == 'POST':

        offer.delete()

        messages.success(
            request,
            'Offer deleted successfully.'
        )

        return redirect('offer_list')

    return render(
        request,
        'offers/offer_delete.html',
        {'offer': offer}
    )


# =========================
# LATEST UPDATE CRUD
# =========================

@login_required
def latest_update_list(request):

    updates = LatestUpdate.objects.all()

    return render(
        request,
        'updates/update_list.html',
        {'updates': updates}
    )


@login_required
def latest_update_create(request):

    form = LatestUpdateForm()

    if request.method == 'POST':

        form = LatestUpdateForm(
            request.POST,
            request.FILES
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Update created successfully.'
            )

            return redirect('latest_update_list')

    return render(
        request,
        'updates/update_create.html',
        {'form': form}
    )


@login_required
def latest_update_update(request, pk):

    update = get_object_or_404(
        LatestUpdate,
        pk=pk
    )

    form = LatestUpdateForm(
        instance=update
    )

    if request.method == 'POST':

        form = LatestUpdateForm(
            request.POST,
            request.FILES,
            instance=update
        )

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Update updated successfully.'
            )

            return redirect('latest_update_list')

    return render(
        request,
        'updates/update_update.html',
        {
            'form': form,
            'update': update
        }
    )


@login_required
def latest_update_delete(request, pk):

    update = get_object_or_404(
        LatestUpdate,
        pk=pk
    )

    if request.method == 'POST':

        update.delete()

        messages.success(
            request,
            'Update deleted successfully.'
        )

        return redirect('latest_update_list')

    return render(
        request,
        'updates/update_delete.html',
        {'update': update}
    )