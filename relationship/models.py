from django.db import models

class Employee(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    mobile = models.IntegerField()
    
    
    def __str__(self):
        return self.first_name 
    
class Project(models.Model):
    project = models.CharField(max_length =100)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.project
    
class Manager(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField()
    mobile = models.IntegerField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.first_name+' '+self.last_name+' '+self.email+' '+str(self.mobile)