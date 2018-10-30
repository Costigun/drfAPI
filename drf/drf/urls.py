"""drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:фывфывыф
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
from django.conf.urls import url,include
from django.urls import path
from rest_framework import routers
from rest import views
from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
# router.register(r'Contacts',views.ContactsViewSet
router.register(r'',views.CourseViewSet)
urlpatterns = [
    url('admin/', admin.site.urls),
    url('^',include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('contacts', views.ContactsViewSet.as_view()),
    path('branches', views.BranchesViewSet.as_view()),
    path('category' ,views.CategoryViewSet.as_view()),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)