from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from chicken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', views.contact_us, name='contact_us'),

    path('admin/enquiries/', views.enquiry_dashboard, name='enquiry_dashboard'),
    path('admin/enquiries/list/', views.enquiry_list, name='enquiry_list'),
    path('admin/enquiries/<int:pk>/', views.enquiry_detail, name='enquiry_detail'),
    path('admin/enquiries/<int:pk>/update/', views.enquiry_update, name='enquiry_update'),
    path('admin/enquiries/<int:pk>/delete/', views.enquiry_delete, name='enquiry_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)