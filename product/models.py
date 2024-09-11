from django.db import models

#Categories of Product
class Category(models.Model):
    name= models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.name
    
    #This changes the name "Categorys" to "Categories" in DB.
    class Meta:
        verbose_name_plural = 'Categories'


#All of our products
class Product(models.Model):
    name= models.CharField(max_length=100,unique=True)
    price= models.DecimalField(default=0, decimal_places=2, max_digits=10)
    category= models.ForeignKey(Category,on_delete=models.CASCADE, default=1)
    description= models.CharField(max_length=250, default="", blank=True, null=True)
    image= models.ImageField(upload_to='product/')

    #add sales
    is_sale= models.BooleanField(default=False)
    sale_price= models.DecimalField(default=0, decimal_places=2, max_digits=10)
    out_of_stock= models.BooleanField(default=False)

    def __str__(self):
        return self.name