from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http  import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.db.models.signals import post_save
from .models import CompanyProfile, Product
from .forms import CreateProductForm,CompanySignUpForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Product,Category
from django.views.generic import TemplateView,CreateView

# Create your views here.
from django.contrib.auth import get_user_model
User = get_user_model()

def save_profile(sender, instance, **kwargs):
    instance.CompanyProfile.save()
    
    post_save.connect(save_profile, sender=User)

class SignUpView(TemplateView):
    template_name = "registration/signit.html"

def recycler_home(request):
    return render(request, 'home.html')

def search(request):
    """
    This view function will serach for available products
    """
    if request.GET['search']:
        search_term = request.GET.get("search")
        products = CompanyProfile.find_profile(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "products":products})
    else:
        message = "It seems you have not searched for anything ..."
        
        return render(request, 'search.html',{"message":message})

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
def create_product(request):
    """
    This view function creates an instance of a product
    """      
    if request.method == 'POST':
        form = CreateProductForm(request.POST)
        if form.is_valid():
            products = form.save(commit = False)
            products.user = request.user
            products.save()
            messages.success(request, 'Product created successfully !!')
        return redirect('profile')
    else:
        form = CreateProductForm()
        return render(request, 'edit.html',{"form":form})

def product(request):
    categories = Category.objects.all()
    return render(request, 'index.html',{"categories":categories})

class CompanySignUpView(CreateView):
    model = User
    form_class = CompanySignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('profile')