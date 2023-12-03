from django.db import models

# Create your models here.

class XUser(models.Model):
    
    username = models.CharField()
    real_name = models.CharField()
    age = models.IntegerField()
    id_card_no = models.CharField()
    brithday = models.DateField()
    active = models.BooleanField()
    
    class Meta:
        db_table = "x_user"