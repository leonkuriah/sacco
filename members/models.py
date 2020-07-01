from django.db import models
from django.urls import reverse

class Members(models.Model):
    memberid = models.IntegerField()
    membername = models.CharField(max_length=30)
    contribution = models.IntegerField()

    def __str__(self):
        return self.membername

    def get_absolute_url(self):
        return reverse('members_edit', kwargs={'pk': self.pk})

# Create your models here.
