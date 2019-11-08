from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.http  import HttpResponse,Http404,HttpResponseRedirect,JsonResponse
from django.db.models.signals import post_save
from .models import RecyclerProfile, Product
from .forms import CreateProductForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login
from django.contrib import messages
from .models import Product

# Create your views here.
def save_profile(sender, instance, **kwargs):
    instance.RecyclerProfile.save()
    
    post_save.connect(save_profile, sender=User)

def recycler_home(request):
    return render(request, 'home.html')

def search(request):
    """
    This view function will serach for available products
    """
    if request.GET['search']:
        search_term = request.GET.get("search")
        products = Product.search_product(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message, "products":products})
    else:
        message = "You have not searched for anything yooow ..."
        
        return render(request, 'search.html',{"message":message})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'registration/register.html', context)

@login_required(login_url ="/recycler/accounts/login")
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
        return render(request, 'create.html',{"form":form})

def product(request):
    products = Product.objects.all()