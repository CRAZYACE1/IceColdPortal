from django.db import models


# Create your models here.


class Brother(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    crossing_date = models.CharField(max_length=20)
    ship_name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s %s' % (self.first_name, self.last_name, self.crossing_date, self.ship_name)
