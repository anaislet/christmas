from django.db import models
from authentication.models import Member, Family

class Gift(models.Model):
    class Price(models.TextChoices):
        PRICE1 = "Moins de 40 €"
        PRICE2 = "Entre 40 et 100 €"
        PRICE3 = "Plus de 100€"

    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    family = models.ForeignKey(Family, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    link = models.URLField(null=True, blank=True)
    price = models.CharField(choices=Price.choices, max_length=20)

    def __str__(self):
        return self.name
    
class Purchase(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    gift = models.ForeignKey(Gift, on_delete=models.CASCADE)