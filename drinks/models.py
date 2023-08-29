from django.db import models

class Drink(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.name + ', ' + self.desc
    
class Food(models.Model):
    # id = models.IntegerField(primary_key=True)
    food_name = models.CharField(max_length=100)
    food_desc = models.CharField(max_length=100)
    