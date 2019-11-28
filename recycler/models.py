from django.db import models
# from django.contrib.auth.models import AbstractUser
from recycle.models import User

# Create your models here.
class CompanyProfile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    bio = models.CharField(max_length = 30, blank = True)

    def __str__(self):
        return f'{user.username}\'s Profile'

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profile = CompanyProfile.objects.all()
        return profile

    @classmethod
    def find_profile(cls, search_term):
        profile = cls.objects.filter(user__username__icontains=search_term)
        return profile

    @classmethod
    def update_profile(cls, id, bio):
        updated = CompanyProfile.objects.filter(id=id).update(bio=bio)
        return updated
        
class Category(models.Model):
    name = models.TextField(max_length = 20)

    def __str__(self):
        return self.name
        
    def delete_category(self):
	    self.delete()
        
class Product(models.Model):
    name = models.TextField(max_length = 20)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    category = models.ForeignKey(Category, on_delete = models.CASCADE)
    description = models.TextField(max_length = 500, default = 'No description provided')
    mode_of_recycling = models.TextField(max_length = 50, default = 'Send to our drop off points')
    def __str__(self):
        return self.name
        
    def delete_product(self):
	    self.delete()

    @classmethod
    def search_product(cls, search_term):
        products = cls.objects.filter(name__icontains = search_term)
        return products

class Blog(models.Model):
    name = models.TextField(max_length = 20)
    body = models.TextField(max_length= 400)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
