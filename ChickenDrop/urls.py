from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from chicken import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('about/', views.about, name='about'),
    path('terms-and-conditions/', views.terms_conditions, name='terms_conditions'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),

    path('contact/', views.contact_us, name='contact_us'),

    path('enquiries/', views.enquiry_dashboard, name='enquiry_dashboard'),
    path('enquiries/list/', views.enquiry_list, name='enquiry_list'),
    path('enquiries/<int:pk>/', views.enquiry_detail, name='enquiry_detail'),
    path('enquiries/<int:pk>/update/', views.enquiry_update, name='enquiry_update'),
    path('enquiries/<int:pk>/delete/', views.enquiry_delete, name='enquiry_delete'),
    path(
        'dashboard/offers/',
        views.offer_list,
        name='offer_list'
    ),
    path(
        'dashboard/offers/create/',
        views.offer_create,
        name='offer_create'
    ),

    path(
        'dashboard/offers/<int:pk>/update/',
        views.offer_update,
        name='offer_update'
    ),

    path(
        'dashboard/offers/<int:pk>/delete/',
        views.offer_delete,
        name='offer_delete'
    ),

    # =====================
    # LATEST UPDATES CRUD
    # =====================

    path(
        'dashboard/updates/',
        views.latest_update_list,
        name='latest_update_list'
    ),

    path(
        'dashboard/updates/create/',
        views.latest_update_create,
        name='latest_update_create'
    ),

    path(
        'dashboard/updates/<int:pk>/update/',
        views.latest_update_update,
        name='latest_update_update'
    ),

    path(
        'dashboard/updates/<int:pk>/delete/',
        views.latest_update_delete,
        name='latest_update_delete'
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)