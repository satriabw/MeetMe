from django.db import models
from account.models import *
# Create your models here.

class InterestMatrix(models.Model):
    interest = models.ForeignKey(Interest, null=True, related_name="interest_matrix")
    interest_pair = models.ForeignKey(Interest, null=True, related_name="interest_pair_matrix")
    weight = models.DecimalField(null=True, max_digits=10, decimal_places=6)

    def __str__(self):
        return self.interest.interest + ":" + self.interest_pair.interest + ":" + self.weight