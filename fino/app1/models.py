from django.db import models
from django.contrib.auth.models import User
from calendar import monthrange
import calendar
import datetime


CATEGORY = (
    ('Food', 'Bills'),
    ('Travel', 'Shopping'),
    ('HealthCare', 'Other'),
)

class Details(models.Model):
    
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    curbal = models.PositiveIntegerField(default = 0)
    image = models.ImageField(default='adminp.jpg', upload_to='Profile_Images')
    dail_el = models.PositiveIntegerField(default=0)
    Today_ex = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    badge = models.CharField(max_length=100)

    def __str__(self):
        p=self.curbal
        return str(self.curbal)
    def dail_el(self):
        now=datetime.datetime.now()
        p=calendar.monthrange(now.year,now.month)[1]
        dail_el=(self.curbal // (p-now.month))-100
        return dail_el
    def badge(self):
        if self.curbal>90000:
            badge="Platinum"
        elif self.curbal>50000:
            badge="Gold"
        elif self.curbal>1000:
            badge="Silver"
        else:
            badge="none"
        return badge
    
    
class Transactions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # curbal = models.ForeignKey(Details, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(null=True)
    payment = models.CharField(max_length=100)
    category = models.CharField(max_length=50, choices=CATEGORY, null=True)

    def __str(self):
        return f'{self.curbals} ordered by {self.date}'
    

class todolist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.CharField(max_length=100)

