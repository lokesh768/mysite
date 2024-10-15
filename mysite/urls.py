
from django.contrib import admin
from django.urls import path, include
from users import views as users_views
from django.contrib.auth import views as authentication_views
from django.conf import settings
from django.conf.urls.static import static
from food.views import Welcome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',Welcome,name='welcome'),
    path('food/', include('food.urls')),
    path('register/', users_views.register, name="register"),
    path('login/', authentication_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', authentication_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', users_views.profilepage, name='profile')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
