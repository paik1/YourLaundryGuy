from django.db import models
from datetime import datetime, date
#from django.contrib.auth.models import User
#from django.core.validators import RegexValidator
# Create your models here.

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

class OrderInfo(models.Model):
    name  = models.CharField(max_length=20,)
    email = models.EmailField(max_length=30,)
    phone_number = models.CharField(max_length=10,)
    categories = models.CharField(max_length=21, choices=CATEGORIES, default='waf')
    time_slot = models.CharField(max_length=23, choices=TIME_SLOTS, default='plz')
    order_date = models.DateField(null = 'true')

    def __str__(self):
        return self.name + " - " + str(self.order_date)