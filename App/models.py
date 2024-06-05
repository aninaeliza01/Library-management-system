from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    USER_TYPES = (
        ('ADMIN', 'Admin'),
        ('USER', 'User'),
    )

    user_type = models.CharField(
        max_length=20,
        choices=USER_TYPES,
        blank=True,
        null=True,
        default='USER'
    )


    username = models.CharField(max_length=50, unique=True)
    is_user = models.BooleanField(default=True)

    REQUIRED_FIELDS = []

    def __str__(self):
        return self.username
    

class Membership(models.Model):
    MEMBERSHIP_CHOICES = [
        ('six_months', 'Six Months'),
        ('one_year', 'One Year'),
        ('two_years', 'Two Years'),
    ]

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=100)
    contact_address = models.CharField(max_length=255)
    aadhar_card_no = models.CharField(max_length=12)
    start_date = models.DateField()
    end_date = models.DateField()
    membership_type = models.CharField(max_length=20, choices=MEMBERSHIP_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.membership_type}"
    

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100) 
    category = models.CharField(max_length=100)  
    status = models.CharField(max_length=50)  
    cost = models.DecimalField(max_digits=10, decimal_places=2)  
    procurement_date = models.DateField()
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100) 
    genre = models.CharField(max_length=100)  
    status = models.CharField(max_length=50)  
    cost = models.DecimalField(max_digits=10, decimal_places=2) 
    procurement_date = models.DateField()
    quantity = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name


class Issue(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE,null=True)
    date_of_issue = models.DateField()
    date_of_return = models.DateField()
    status = models.CharField(max_length=50)

class Return(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE,null=True)
    date_of_issue = models.DateField()
    date_of_return = models.DateField()
    fine_calculation = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    status = models.CharField(max_length=50)

class Request(models.Model):
    membership = models.ForeignKey(Membership, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, null=True, blank=True, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, null=True, blank=True, on_delete=models.CASCADE)
    requested_date = models.DateField()
    request_fulfilled_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=50)