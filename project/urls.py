"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
#import settings
from django.conf import settings
#import static
from django.conf.urls.static import static

#import app urls
import home.urls
import about.urls
import products.urls
import suppliers.urls
import contact.urls
import sustainability.urls
import innovation.urls
import gallary.urls
import news.urls
import journalist.urls
urlpatterns = [
    
    path("admin/", admin.site.urls),
    path("",include(home.urls)),
    path("about/",include(about.urls)),
    path("products/",include(products.urls)),
    path("suppliers/",include(suppliers.urls)),
    path("contact/",include(contact.urls)),
    path("sustainability/",include(sustainability.urls)),
    path("innovation/",include(innovation.urls)),
    path("gallary/",include(gallary.urls)),
    path("news/",include(news.urls)),
    path("journalist/",include(journalist.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




