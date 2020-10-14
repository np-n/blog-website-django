from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    image = models.ImageField(default = 'default.jpg',upload_to = 'profile_pics')


    def __str__(self):
        return f'{self.user.username} profile'


# Not resized why?
# This is run after model is saved to resize image
def save(self, *args, **kwargs):
    # running save method of parent class
    # super().save()
    super().save(*args, **kwargs)
    img = Image.open(self.image.path)
    if img.height > 300 or img.width > 300 :
        output_size =(300,300)
        # Resize image
        img.thumbnail(output_size)
        # save resized image to it's location/path
        img.save(self.image.path)
