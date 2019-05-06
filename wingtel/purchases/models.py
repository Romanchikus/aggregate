from model_utils import Choices
from django.contrib.auth.models import User
from django.db import models


class Purchase(models.Model):
    STATUS = Choices(
        ('pending', 'Pending'),
        ('overdue', 'Past Due'),
        ('complete', 'Complete'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT)

    status = models.CharField(max_length=20, choices=STATUS, default=STATUS.pending)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    payment_date = models.DateTimeField(null=True, db_index=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)