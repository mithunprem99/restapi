from django.db import models


# Create your models here.
class Customer(models.Model):
	c_name = models.CharField(max_length=255)
	c_address = models.TextField()
	c_email = models.EmailField()
	c_phno = models.CharField(max_length=15)
	c_active= models.BooleanField()

	def __str__(self):
		return self.c_name 


class Products(models.Model):
	p_name = models.CharField(max_length=255)
	p_description=models.TextField()
	c_id= models.ForeignKey(Customer,on_delete=models.CASCADE)
	p_type= models.CharField(max_length=255)
	p_price= models.IntegerField()
	p_image= models.ImageField(upload_to='customer')
	p_add_date=models.DateTimeField(auto_now_add=True,auto_now=False,blank=True)
	# p_add_date=models.DateField(auto_now_add=True,auto_now=False,blank=True)
	# p_add_date=models.DateTimeField()
	p_status= models.BooleanField()



	 # 06a1bb7c7ae975127397832f989a5d7fbc0deace


	 # end point: 06a1bb7c7ae975127397832f989a5d7fbc0deace