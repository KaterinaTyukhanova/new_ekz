from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.LoginServerView.as_view(), name='login'),
    path('logout/', views.LogoutServerView.as_view(), name='logout'),
    path('service/', views.service, name='service'),
    path('service/<int:pk>', views.service_detail, name='service-detail'),
    path('register/', views.SignUpView.as_view(), name="register"),
    path('profile/', views.profile, name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)