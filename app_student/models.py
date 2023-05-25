from django.db import models


# Create your models here.
class Students(models.Model):

    list_promo = [("L1-I", "Licence 1 Info"), ("L1-F", "Licence 1 Fisc"), ("L2-C", "Licence 2 Conception"), ("L2-R", "Licence 1 Reseau")]
    list_genre = [("M", "Monsieur"), ("F", "Madame")]
    name = models.CharField(max_length=255, unique=True)
    age = models.IntegerField(default=0)
    genre = models.CharField(max_length=1, choices=list_genre, default="aucun")
    promotion = models.CharField(max_length=7, choices=list_promo, default="L1-I")
    status = models.CharField(max_length=255, default="encours")
    is_active = models.BooleanField(default=True)


