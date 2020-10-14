"""django_project_0 URL Configuration

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
from django.contrib import admin
from django.urls import path,include
from users import views as user_view
from django.contrib.auth import views as auth_views
# To serve uploaded static files
from django.conf import settings
from django.conf.urls.static import static

# urlpatterns = [
#     # ... the rest of your URLconf goes here ...
# ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/',include('blog.urls')),
    # To ensure / and about/ works same as blog/ and blog/about/
    # We want to use blog home page as home page in our website
    path('',include('blog.urls')),

    # Alternative approach to routing without creating views.py file in app
    # instead we import views in main project urls.py
    path('register/',user_view.register,name='register'),

    # setting  django default login and logout route
    path('login/',auth_views.LoginView.as_view(template_name = 'users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name = 'users/logout.html'),name='logout'),

    path('profile/',user_view.profile,name='profile'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
