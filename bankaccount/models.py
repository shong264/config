from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from .utils import Helper

# Create your models here.

class BankAccount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="bankaccount")
    account_number = models.CharField(max_length=20, unique=True, blank=True)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00 ,validators=[MinValueValidator(0.00)])
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = 'BankAccount'
        constraints = [
            models.CheckConstraint(
                check=models.Q(balance__gte=0.00),
                name='check_balance',
            )
        ]
        indexes = [
            models.Index(fields=['balance']),
        ]

    def __str__(self):
        return f'{self.user.username} - {self.account_number}'
    
    def save(self, *args, **kwargs):
        if not self.account_number:
            self.account_number = Helper.generate_account_number(prefix='EG')
        super().save(*args, **kwargs)

