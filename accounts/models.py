from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    mobile = models.CharField(max_length=12, null=True)
    phone_number = models.CharField(max_length=12, null=True)
    company = models.CharField(max_length=100, null=True)
    address_line1 = models.CharField(max_length=100, null=True)
    address_line2 = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)
    zip_code = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)
    user_type = models.CharField(max_length=20, help_text='1) BI => Bidder,'
                                                          '2) VE => Vendor', null=True)
    date_joined = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'custom_user'