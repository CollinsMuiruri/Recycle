from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
# The models that differentiate users start here

class User(AbstractUser):
    is_consumer = models.BooleanField(default = False)
    is_company = models.BooleanField(default = False)


# The models that differentiate users start here
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(default = 'default.jpg', upload_to = 'profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    photo_caption = models.CharField(max_length=140)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-pub_date']

    def __str__(self):
        return self.photo_caption

    def save_photo(self):
        self.save()

    @classmethod
    def get_photos(cls):
        photos = Photo.objects.all()
        return photos

