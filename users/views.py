from django.shortcuts import render, redirect
from django.views import View
from .forms import UserRegisterForm

# Create your views here.


class RegisterView(View):
    """HTTP Method request callback functions"""

    def get(self, request):
        form = UserRegisterForm()
        return render(request, 'users/register.html',
                      # take `UserRegisterForm ` for render pre-built reg page
                      {'form': form})

    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('index')
