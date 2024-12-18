from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.listing_list, name='listings'),
    path('listings/<int:pk>/', views.listing_retrieve, name='listing'),
    path('add-listing/', views.listing_create, name='listing_create'),
    path('listings/<int:pk>/edit/', views.listing_update, name='listing_update'),
    path('listings/<int:pk>/delete/', views.listing_delete, name='listing_delete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)