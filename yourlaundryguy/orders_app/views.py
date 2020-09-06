from django.shortcuts import render
from .forms import UserForm
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect


# Create your views here.
class PlaceOrderView(TemplateView):
    template_name = 'order.html'


    def get(self, request):
        form = UserForm()
        return render(request, self.template_name, {'form': form})


    def post(self, request):
        form = UserForm(request.POST)
        if form.is_valid():
            print("form is valid")
            form.save()
            print("Post successfull")
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

def HomeView(request):
    template_name = 'home.html'
    return render(request, template_name)


