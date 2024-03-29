from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),
    path('register/',views.register,name="register"),
    path('login/',views.loginPage,name="login"),
    path('logout/',views.logoutUser,name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

