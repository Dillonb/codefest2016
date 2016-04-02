from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager

# Create your models here.

class UVMUserManager(BaseUserManager):
    def _create_user(self, netid, password, first_name=None, last_name=None, uvm_email=None, full_name=None, department=None):
        if not netid:
            raise ValueError("Netid must be set")

        user = self.model(netid=netid, first_name=first_name, last_name=last_name, full_name=full_name, department=department)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, netid, password=None, **extra_fields):
        return self._create_user(netid,password, **extra_fields)

    def create_superuser(self, netid, password=None, **extra_fields):
        return self._create_user(netid, password, **extra_fields)

class UVMUser(AbstractBaseUser):
    """A custom user model to represent a UVM student."""
    netid = models.CharField(max_length=8,unique=True)
    first_name = models.CharField(max_length=40,null=True)
    last_name = models.CharField(max_length=40,null=True)
    uvm_email = models.CharField(max_length=40,null=True)
    full_name = models.CharField(max_length=150,null=True)
    department = models.CharField(max_length=40,null=True)

    facebook_url = models.CharField(max_length=100, null=True)
    additional_email_1 = models.CharField(max_length=100, null=True)
    additional_email_2 = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=14, null=True)
    #user_picture goes here later

    USERNAME_FIELD = 'netid'
    objects = UVMUserManager()

class Comment(models.Model):
    user = models.ForeignKey("UVMUser")
    event = models.ForeignKey("Event")
    content = models.TextField()
    time = models.DateTimeField(auto_now=True)

class Club(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey("UVMUser", null=True)

class Event(models.Model):
	"""A custom event model to represent events around UVM Campus"""
	USER = "U"
	CLUB = "C"
	USER_TYPES = (
		(USER, 'user'),
		(CLUB, 'club')
	)

	name = models.CharField(max_length=40)
	latitutde = models.FloatField(null=True)
	longitube = models.FloatField(null=True)
	user_type = models.CharField(max_length=1,choices=USER_TYPES)
	date_time = models.DateTimeField(null=True)
	description = models.CharField(max_length=255)


	user = models.ForeignKey("UVMUser")
