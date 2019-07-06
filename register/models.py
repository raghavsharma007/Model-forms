from django.db import models

class FillDetails(models.Model):
    client_name = models.CharField(max_length=100, null=True, blank=True)
    date = models.DateField()
    choice = models.CharField(choices=(('Yes','Yes'),('No','No')),default='No',max_length=10)

    def __str__(self):
            return '%s %s %s' % (self.client_name, self.date, self.choice)

