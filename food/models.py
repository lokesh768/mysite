from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Item(models.Model):

    def __str__(self):
        return self.item_name
    
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_description = models.CharField(max_length=400)
    item_price = models.IntegerField()
    item_image = models.ImageField(default='comingsoon.jpg', upload_to='item_pictures')

    def get_absolute_url(self):
        return reverse("food:detail", kwargs={"pk": self.pk})
    


