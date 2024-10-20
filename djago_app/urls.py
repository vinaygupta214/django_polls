from django.contrib import admin
from django.urls import path , include
from djago_app import views

# handler404 = 'djago_app.views.handler404'

urlpatterns = [
    path('admin/',admin.site.urls),
    path('polls/',include('polls.urls')),
    path('api/',include('polls.api_urls')),
    path('accounts/',include('accounts.urls')),
]




