from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_app.urls')),
    #include the built-in auth urls for the built-in view
    path('accounts/',include('django.contrib.auth.urls')),
]
