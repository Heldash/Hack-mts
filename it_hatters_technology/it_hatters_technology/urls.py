"""
URL configuration for it_hatters_technology project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from agregate_company.views import add_test_database
from drf_spectacular.views import SpectacularSwaggerView,SpectacularAPIView
urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/",include("agregate_company.urls")),
    path("api/schema/",SpectacularAPIView.as_view(),name="api_schema"),
    path("api/doc/",SpectacularSwaggerView.as_view(url_name="api_schema"),name="api_schema"),
    path("create_test/",add_test_database,name = "add_test")
]
