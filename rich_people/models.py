from django.db import models


class RichPerson(models.Model):
    name = models.CharField(max_length=200)
    money = models.DecimalField(help_text='In billions of dollars', max_digits=10, decimal_places=2)

    def __str__(self):
        return '{}-{}'.format(self.name, self.money)
