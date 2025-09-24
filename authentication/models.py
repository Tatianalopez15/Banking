from django.db import models

# Create your models here.
class Country(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name="departments")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class City(models.Model):
    name = models.CharField(max_length=100)
    abrev = models.CharField(max_length=10, blank=True, null=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="cities")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
class User(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50, blank=True, null=True)
    mobile_phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.TextField()
    city = models.ForeignKey(City, on_delete=models.SET_NULL, null=True, related_name="users")
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname or ''}"