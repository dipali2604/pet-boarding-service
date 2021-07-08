from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices


# Create your models here.
class PetRegister(models.Model):
    PET_CHOICES = (
            ('Dog','Dog'),
            ('Cat','Cat'),
            ('Fish','Fish'),
            ('Turtle','Turtle'),
            ('Horse','Horse'),

 )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    pettype = models.CharField( max_length = 100, choices = PET_CHOICES)
    photo = models.ImageField(upload_to = 'petboarding' )
    age = models.PositiveIntegerField()
    description = models.TextField()
    specialinstruction = models.TextField()

    def __str__(self):
            return self.user

          
 
class Owner(models.Model):
    GENDER_CHOICES = (
            ('Male','Male'),
            ('Female','Female'),
            ('Others','Others'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 254)
    contact = models.CharField(max_length = 12)
    gender = models.CharField(max_length = 50, choices= GENDER_CHOICES)
    dob = models.DateField(max_length=10)
    photo = models.ImageField(upload_to = 'petboarding' )
    altcontact = models.CharField(max_length = 12)
    address = models.CharField(max_length =80)
    city = models.CharField(max_length = 30)
    pincode = models.IntegerField()

    def __str__(self):
            return self.user

class Boarding(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        duration = models.PositiveIntegerField()
        chargeamount = models.FloatField()
        is_payment_complete = models.BooleanField()
        is_pet_dlv_back = models.BooleanField()
        date = models.DateTimeField(auto_now = True)

        def __str__(self):
            return self.user


class Payment(models.Model):
        PAYMENT_CHOICES = (
                ('Cash On Delivery','Cash On Delivery'),
                ('Other UPI IDs', 'Other UPI IDs'),

        )
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        payment_method = models.CharField(max_length=30,choices=PAYMENT_CHOICES)
        amountpaid =models.FloatField()
        is_done = models.BooleanField()
        date = models.DateTimeField(auto_now= True)

        def __str__(self):
            return self.user

class Review(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        rating = models.IntegerField()
        review = models.TextField()
        date = models.DateTimeField(auto_now= True)

        def __str__(self):
            return self.user

class Notification(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        photo = models.ImageField(upload_to = '' )
        update_on = models.DateTimeField(auto_now= True)

        def __str__(self):
            return self.user

class Complaints(models.Model): 
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        subject = models.CharField(max_length = 100)
        detail = models.TextField()
        date = models.DateTimeField(auto_now = True)
        is_resolved = models.BooleanField()


        def __str__(self):
            return self.user

