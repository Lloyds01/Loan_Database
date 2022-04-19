from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin



class CustomUserManager(BaseUserManager):

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('email field is required')

        # cleaning the email to the required format
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)  # create the user
        user.set_password(password)  # setting the password fo user
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('name', 'admin')

        if extra_fields.get("is_staff") is not True:
            raise ValueError('superuser must have is_staff=True')

        if extra_fields.get("is_superuser") is not True:
            raise ValueError('superuser must have is_superuser=True')

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []
    objects = CustomUserManager()


    def __str__(self):
        return self.email

class Liberty_Loan_database(models.Model):

    Full_Name	            = models.CharField(max_length=60)
    Borrower_Mobile         = models.CharField(max_length=30)
    Borrower_Age		    = models.IntegerField()
    Borrower_Gender         = models.CharField(max_length=10)
    BVN	                    = models.CharField(max_length=15)	
    Loan_Duration	        = models.CharField(max_length=30)
    Days_Past_Maturity	    = models.CharField(max_length=15)
    Last_Repayment	        = models.FloatField()
    Principal_Amount	    = models.FloatField()
    Balance_Amount	        = models.FloatField()
    Loan_Status_Name	    = models.CharField(max_length=30)

    def __str__(self):
        return self.BVN


    class Meta:
        ordering = ["-Full_Name"]



class Bvn_check(models.Model):
    bvn = models.CharField(max_length=15)


    def __str__(self):
        return self.bvn