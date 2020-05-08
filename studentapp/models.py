from django.db import models
from django.contrib.auth.models import User
from io import BytesIO
from PIL import Image
from django.core.files import File
from datetime import datetime
# Create your models here.

def compress(image):
    im = Image.open(image)
    # create a BytesIO object
    im_io = BytesIO()
    # save image to BytesIO object
    im.save(im_io, 'JPEG', quality=70)
    # create a django-friendly Files object
    new_image = File(im_io, name=image.name)
    return new_image


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, null = True, max_length=50)
    user_name = models.CharField(max_length=30, blank=True, null=True)
    user_email = models.CharField(max_length=30, blank=True, null=True)
    user_phone = models.CharField(max_length=30, blank=True, null=True)
    user_picture = models.ImageField(default="profile.png",upload_to='profile_pic', blank=True)
    user_bloodGroup = models.CharField(max_length=30, blank=True, null=True)
    user_gender = models.CharField(max_length=30, blank=True, null=True)
    user_address = models.CharField(max_length=100, blank=True, null=True)
    user_city = models.CharField(max_length=30, blank=True, null=True)
    user_state = models.CharField(max_length=30, blank=True, null=True)
    user_zip = models.CharField(max_length=100, blank=True, null=True)
    user_school = models.CharField(max_length=100, blank=True, null=True)
    user_college = models.CharField(max_length=100, blank=True, null=True)
    user_university = models.CharField(max_length=100, blank=True, null=True)
    user_department = models.CharField(max_length=30, blank=True, null=True)
    user_fbId = models.CharField(max_length=30, blank=True, null=True)
    user_bio = models.TextField(blank=True, null=True)
    date = models.DateField(default=datetime.now)
    bol_field = models.CharField(max_length=30, blank=True, null=True)
    
    
    
    def save(self):
        super().save()

        img = Image.open(self.user_picture.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.user_picture.path)

    @property
    def get_photo_url(self):
        if self.user_picture and hasattr(self.user_picture, 'url'):
            return self.user_picture.url
        else:
            return "/media/profile.png"

  

   

    

