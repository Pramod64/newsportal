from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.
def mycustomvalodator(value):
    if len(value)>5:
        return True
    else:
        raise ValidationError("must have more than 5 characters")
        


class Category(models.Model):
    title = models.CharField(max_length=100, unique=True ,validators=[mycustomvalodator])

    def __str__(self):
        return self.title

class Blog(models.Model):
    title=models.CharField(max_length=100,unique=True)
    description=models.TextField(null=True,blank=True)
    image=models.ImageField(upload_to='blog/',null=True,blank=True)
    created_date=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    
    def __str__(self):
        return self.title
    