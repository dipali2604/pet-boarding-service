from django.db import models
from django.contrib.auth.models import User
from django.db.models.enums import Choices
from django.core.validators import RegexValidator, MaxValueValidator, MinValueValidator
from django.db.models.fields.related import OneToOneField

# Create your models here.
class Pet(models.Model):
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
    photo = models.ImageField(upload_to = 'pets' )
    age = models.PositiveIntegerField()
    description = models.TextField()
    specialinstruction = models.TextField()

    def __str__(self):
            return f"{self.name} [{self.pettype}]"

          
 
class Profile(models.Model):
    GENDER_CHOICES = (
            ('Male','Male'),
            ('Female','Female'),
            ('Others','Others'),
    )
    phoneregex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    user = OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length = 50)
    lastname = models.CharField(max_length = 50)
    email = models.EmailField(max_length = 254)
    phone = models.CharField(max_length=15, validators=[phoneregex], blank=True)
    gender = models.CharField(max_length = 50, choices= GENDER_CHOICES)
    dob = models.DateField(max_length=10)
    photo = models.ImageField(upload_to = 'profile' )
    altcontact = models.CharField(max_length = 12)
    address = models.TextField(max_length =80)
    city = models.CharField(max_length = 30)
    pincode = models.IntegerField()

    def __str__(self):
            return self.user.username

class Boarding(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        pet = models.ForeignKey(Pet, on_delete=models.CASCADE, related_name='boardings', null=True)
        duration = models.PositiveIntegerField(help_text="enter number of days")
        chargeamount = models.FloatField(default=100.00)
        is_payment_complete = models.BooleanField()
        is_pet_dlv_back = models.BooleanField()
        date = models.DateTimeField(auto_now = True)

        def __str__(self):
            return self.user.username

        def generate_charge_amount(self):       
            return self.duration * 100

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
            return self.user.username

class Review(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        rating = models.IntegerField(validators= [MinValueValidator(1), MaxValueValidator(5)])
        review = models.TextField()
        date = models.DateTimeField(auto_now= True)

        def __str__(self):
            return self.user.username

class Notification(models.Model):
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        photo = models.ImageField(upload_to = '' )
        update_on = models.DateTimeField(auto_now= True)

        def __str__(self):
            return self.user.username

class Complaint(models.Model): 
        user = models.ForeignKey(User, on_delete=models.CASCADE)
        subject = models.CharField(max_length = 100)
        detail = models.TextField()
        date = models.DateTimeField(auto_now = True)
        is_resolved = models.BooleanField()


        def __str__(self):
            return self.user.username

