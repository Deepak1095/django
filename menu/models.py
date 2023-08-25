from django.db import models
import uuid
# Create your models here.

class DishModel(models.Model):
    dishId = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    name = models.CharField(max_length=20)
    price = models.IntegerField()