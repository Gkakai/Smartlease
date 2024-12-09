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

class PropertyOwner(models.Model):
     name = models.CharField(max_length=100)
     email = models.EmailField(max_length=254)
     phone = models.CharField(max_length=20)
     description = models.TextField()
     image = models.ImageField(upload_to='owners/')
     owner_type = models.CharField(max_length=40, default='Real Estate')
     x = models.CharField(max_length=50)
     fb = models.CharField(max_length=50)
     linkedin= models.CharField(max_length=50)
     ig = models.CharField(max_length=50)
     def __str__(self):
          return self.name


class Agent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='agents/', null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    description = models.TextField()
    phone_number = models.CharField(max_length=15, null=True, blank=True)
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    linkedin = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name


class Properties(models.Model):
     name = models.CharField(max_length=100, default=0)
     address = models.CharField(max_length=255, default=0)
     description = models.TextField()
     price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
     city = models.CharField(max_length=100, default=0)
     country = models.CharField(max_length=100, default=0)
     beds = models.CharField(max_length=50, default=0)
     baths = models.CharField(max_length=50, default=0)
     area = models.CharField(max_length=50, default=0)
     owner = models.ForeignKey(PropertyOwner, on_delete=models.CASCADE, related_name='landlord',  null=True, blank=True)
     agent = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='property_agent', null=True, blank=True)
     def __str__(self):
          return self.name
     
class PropertyImages(models.Model):
     property = models.ForeignKey(Properties, on_delete=models.CASCADE, related_name='images')
     image = models.ImageField(upload_to='properties_images/')
     def __str__(self):
          return f"{self.property.name} - {self.id}"


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
     def __str__(self):
          return self.name
   
     
class Service(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField()
     def __str__(self):
          return self.title
     

     
class Property_single(models.Model):
     property = models.ForeignKey(Properties, on_delete=models.CASCADE)
     service = models.ForeignKey(Service, on_delete=models.CASCADE)
     def __str__(self):
          return f"{self.property.name} - {self.service.name}"
     
class Slider(models.Model):
     title = models.CharField(max_length=100)
     image = models.ImageField(upload_to='slider/')
     description = models.TextField()
     def __str__(self):
          return self.name
     
class About_view(models.Model):
     title = models.CharField(max_length=100)
     description = models.TextField()
     def __str__(self):
          return self.title


class Lease_list(models.Model):
     lease = models.ForeignKey(Lease, on_delete=models.CASCADE)
     def __str__(self):
          return self.lease.title

class Testimonial(models.Model) :
     name = models.CharField(max_length=100)
     title = models.CharField(max_length=100)
     description = models.TextField()
     image = models.ImageField(upload_to='testimonial/')
     def __str__(self):
          return self.name
     
     




# Create your models here.
