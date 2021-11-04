from django.db import models
from django.db.models.base import Model

STATE_CHOICE = (
    ('Dhaka', 'Dhaka'),
    ('Khulna', 'Khulna'),
    ('Rajshahi', 'Rajshahi'),
    ('Barisal', 'Barisal'),
    ('Sylhet', 'Sylhet'),
    ('Chattogram', 'Chattogram'),
    ('Rangpur', 'Rangpur')
)
# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(auto_now=False, auto_now_add=False)
    gender = models.CharField(max_length=20)
    locality = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    pin = models.PositiveIntegerField()
    state = models.CharField(choices=STATE_CHOICE, max_length=30)
    mobile = models.PositiveIntegerField()
    email = models.EmailField()
    job_city = models.CharField(max_length=30)
    profile_image = models.ImageField(upload_to='profileImg', blank=True)
    my_file = models.FileField(upload_to='doc', blank=True)