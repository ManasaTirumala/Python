from django.db import models

# Create your models here.
class Topic(models.Model):
    t_name=models.CharField(max_length=280,unique=True)
    
    def __str__(self):
        return self.t_name
    
        
class Page(models.Model):
    p_topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    p_name=models.CharField(max_length=280,unique=True)
    
    def __str__(self):
        return self.p_name
                
class Access(models.Model):
    a_name=models.ForeignKey(Page,on_delete=models.CASCADE)
    a_date=models.DateField(null=True, blank=True)
    def __str__(self):
        return self.a_date