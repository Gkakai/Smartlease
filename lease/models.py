from django.db import models


class Index(models.Model):
     title = models.CharField(max_length=100)
     image = models.ImageField(upload_to='slider/')
     caption = models.CharField(max_length=100)
     order = models.PositiveIntegerField()
def __str__(self):
     return self.title

class About(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField()
     def __str__(self):
          return self.title
     
class Properties(models.Model):
     name = models.CharField(max_length=100)
     address = models.CharField(max_length=255)
     description = models.TextField()
     price = models.DecimalField(max_digits=10, decimal_places=2)
     location = models.CharField(max_length=100)
     def __str__(self):
          return self.name
     

class Lease(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField()
     price = models.DecimalField(max_digits=10, decimal_places=2)
     image = models.ImageField(upload_to='lease/')
     def __str__(self):
          return self.title

class Contact(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField(max_length=254)
     phone = models.CharField(max_length=20)
     message = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)
     def __str__(self):
          return self.name
     def get_absolute_url(self):
          return reverse('contact_detail', kwargs={'pk': self.pk})
     def get_update_url(self):
          return reverse('contact_update', kwargs={'pk': self.pk})
     def get_delete_url(self):
          return reverse('contact_delete', kwargs={'pk': self.pk})
     def get_contact_info(self):
          return f"{self.name} - {self.email}"
     
class Services(models.Model):
     name = models.CharField(max_length=100)
     def __str__(self):
          return self.name
     
class Agents(models.Model):
     name = models.CharField(max_length=100)
     image = models.ImageField(upload_to='agents/')
     def __str__(self):
          return self.name
       
     
     
class Property_single(models.Model):
     property = models.ForeignKey(Properties, on_delete=models.CASCADE)
     service = models.ForeignKey(Services, on_delete=models.CASCADE)
     def __str__(self):
          return f"{self.property.name} - {self.service.name}"
     
class Slider(models.Model):
     title = models.CharField(max_length=100)
     image = models.ImageField(upload_to='slider/')
     description = models.TextField()
     def __str__(self):
          return self.name

class Properties_list(models.Model):
     image = models.ImageField(upload_to='properties_list/')
     price = models.CharField(max_length=100)
     address =models.CharField(max_length=100)
     city = models.CharField(max_length=100)
     country = models.CharField(max_length=100)
     beds = models.CharField(max_length=50)
     baths = models.CharField(max_length=50)
     area = models.CharField(max_length=50)
     def __str__(self):
          return self.price
     
class Lease_list(models.Model):
     lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
     def __str__(self):
          return self.lease.title    
     




# Create your models here.
