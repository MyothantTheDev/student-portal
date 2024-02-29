from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Section(models.Model):
    section = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.section

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    section = models.ManyToManyField(Section, blank=True)
    image = models.ImageField(default='default.jpg', upload_to="profile_pics")

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class Message(models.Model):
    to = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, )
    message = models.TextField(null=False)
    readed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.to} - message'