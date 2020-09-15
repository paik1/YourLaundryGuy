from django.db import models
from datetime import datetime, date
import uuid
from django.contrib.auth.models import User


CATEGORIES = (
    ('waf','WASH AND FOLD'),
    ('wai', 'WASH AND IRON'),
    ('ironing','IRONING'),
    ('dc','DRY CLEANING'),
    ('wfi','WASH FOLD AND IRONING'),
)

TIME_SLOTS = (
    ('plz','PLEASE SELECT A TIME SLOT'),
    ('9t10','9AM-10AM'),
    ('10t11','10AM-11AM'),
    ('11t12','11AM-12PM'),
    ('12t1','12PM-1PM'),
    ('1t2','1PM-2PM'),
    ('2t3','2PM-3PM'),
    ('3t4','3PM-4PM'),
    ('4t5','4PM-5PM'),
    ('5t6','5PM-6PM'),
    ('6t7','6PM-7PM'),
    ('7t8','7PM-8PM'),
    ('8t9','8PM-9PM'),
)

ORDER_STATUS = (
    ('P', 'Placed'),
    ('C', 'Collected'),
    ('D', 'Delivered'),
    ('X', 'Cancelled'),
)

EXPRESS_DELIVERY = (
    ('Y', 'YES'),
    ('N', 'NO')
)

class OrderInfo(models.Model):
    order_id = models.CharField(max_length=100, blank=True, unique=True, default=uuid.uuid4)
    name = models.CharField(max_length=20, default=None)
    manager  = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    email = models.EmailField(max_length=30)
    phone_number = models.CharField(max_length=10,)
    categories = models.CharField(max_length=21, choices=CATEGORIES, default='waf')
    time_slot = models.CharField(max_length=23, choices=TIME_SLOTS, default='plz')
    order_date = models.DateField(null = 'true')
    express_d = models.CharField(max_length=10, choices=EXPRESS_DELIVERY, default='N', help_text='Express Delivery might charge you extra. Please check the Pricing tab for more details')
    status = models.CharField(max_length=10, choices=ORDER_STATUS, default='P')
    normal_cloths_quantity = models.CharField(max_length=10, null=True, default=None)
    normal_cloths_kg = models.CharField(max_length=10, null=True, default=None)
    heavy_cloths_quantity = models.CharField(max_length=10, null=True, default=None)
    heavy_cloths_kg = models.CharField(max_length=10, null=True, default=None)
    iron_quantity = models.CharField(max_length=10, null=True, default=None)
    total_amount = models.CharField(max_length=10, null=True, default=None)

    def __str__(self):
        return self.name + " - " + str(self.order_date)