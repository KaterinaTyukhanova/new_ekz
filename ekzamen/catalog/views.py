from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignUpForm, ZakazForm
from .models import Tovar, Zakaz


def index(request):
    tovar_list = Tovar.objects.order_by('-date')[:5]
    return render(request, 'index.html', {'tovar_list': tovar_list})


def service(request):
    product_list = Tovar.objects.all()
    return render(request, 'tovar.html', {'product_list': product_list})


def profile(request):
    order = Zakaz.objects.filter(user=request.user)

    context = {
        "orders": order,
    }

    return render(request, 'profile.html', context)


class LoginServerView(LoginView):
    template_name = 'registration/login.html'
    success_url = reverse_lazy('index')


class LogoutServerView(LoginRequiredMixin, LogoutView):
    template_name = 'registration/logged_out.html'


class SignUpView(CreateView):
    form_class = SignUpForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


def service_detail(request, pk):
    product = get_object_or_404(Tovar, pk=pk)

    if request.method == 'POST':
        form = ZakazForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.product_id = pk
            instance.save()
    else:
        form = ZakazForm(initial={'user': request.user.pk, 'product': pk})

    return render(request, "tovar_detail.html", {'product': product, 'form': form})

