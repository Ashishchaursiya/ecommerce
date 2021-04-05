from django.db import models

# Create your models here.
class Banner(models.Model):
    image=models.ImageField(upload_to="media/images",default='')

class Product(models.Model):
    name = models.CharField(max_length=60)
    price= models.IntegerField(default=0)
    description= models.CharField(max_length=200,default='')
    category = models.CharField(max_length=60,default='')
    shipping = models.CharField(max_length=60,default='Free')
    size =   models.CharField(max_length=60,default='')
    returnable = models.CharField(max_length=20,default='YES')
    image = models.ImageField(upload_to="media/images",default='')  



    def __str__(self):
        return self.name 

class ProductImage(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE) 
    image =  models.ImageField(upload_to="media/images",default='')  

    def __str__(self):
        return self.product.id  

class Order(models.Model):
    order_id=models.AutoField(primary_key=True)
    item = models.CharField(max_length=5000)  
    name=models.CharField(max_length=90)
    size=models.CharField(max_length=90)
    address=models.CharField(max_length=1000)
    state=models.CharField(max_length=111)
    Landmark=models.CharField(max_length=111)
    district=models.CharField(max_length=111)
    pin_code=models.CharField(max_length=111)
    phone=models.CharField(max_length=111,default='')
     
    def __str__(self):
        return '{}'.format(self.order_id)

class updateOrder(models.Model):
    update_id=models.AutoField(primary_key=True)
    order_id=models.IntegerField(default='')
    update_desc=models.CharField(max_length=5000) 
    timestap=models.DateField(auto_now_add=True)         
    
    def __str__(self):
        return self.update_desc