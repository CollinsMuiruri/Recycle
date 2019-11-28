from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from .models import User
from .forms import ConsumerSignUpForm
from django.views.generic import TemplateView,CreateView

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.
def index(request):
    return render(request, 'index.html')

class SignUpView(TemplateView):
    template_name = "registration/signit.html"

class ConsumerSignUpView(CreateView):
    model = User
    form_class = ConsumerSignUpForm
    template_name = 'registration/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'consumer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')

# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)

#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             password = form.cleaned_data['password1']
#             user = authenticate(username = username,password = password)
#             login(request, user)
#             return redirect('index')
#     else:
#         form = UserCreationForm()
#     context = {'form': form}
#     return render(request, 'registration/register.html', context)

@login_required(login_url ="/accounts/login")
def profile(request):
    return render(request, 'profile.html')
