from django.shortcuts import render, redirect
from .forms import UserForm
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
class PlaceOrderView(TemplateView):
    
    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = UserForm(request.POST or None)
        name = request.POST.get("name")
        email = request.POST.get("email")
        if form.is_valid():
            instance = form.save(commit=False)
            order_id = instance.order_id
            instance.name = name
            instance.manager = request.user
            instance.email = email
            instance.save()
            url1 = reverse('success', kwargs={'order_id': order_id})
            return HttpResponseRedirect(url1)

        return render(request, self.template_name, {'form': form})

def HomeView(request):
    template_name = 'home.html'
    return render(request, template_name)

def success(request, order_id):
    template_name = 'success.html'
    return render(request, template_name)


