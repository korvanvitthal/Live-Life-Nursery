"""LiveLifeNursery URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf.urls.static import static
from django.conf import settings


admin.site.site_title='Live-Life-Nursery'
admin.site.site_header='Nursery Login'
admin.site.index_title='Welcome to Live-Life-Nursery'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('nursery/',views.nursery,name='nursery'),
    path('gallery/',views.gallery,name='gallery'),
    path('accounts/', include('accounts.urls')),
    path('store/', include('store.urls')),
    path('cart/', include('carts.urls')),

    # ORDERS
    path('orders/', include('orders.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
