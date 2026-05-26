from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import ContactEnquiry
from .forms import ContactEnquiryForm, ContactEnquiryUpdateForm


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