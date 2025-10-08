from django.db import models
from django.contrib.auth.models import User  # Advanced Authentication in Django


# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True
    )  # Advanced Authentication in Django
    recipe_name = models.CharField(max_length=100)
    recipe_description = models.TextField()
    recipe_image = models.ImageField(upload_to="recipe")
