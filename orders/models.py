from django.db import models

# Create your models here.
class Machine(models.Model): 
    machine_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def machine_name(self):
        return(self.machine_name)

class Client(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def client_name(self):
        return(self.client_name)

class Order(models.Model):
    order_name = models.CharField(max_length=100)
    order_quantity = models.IntegerField(blank=True)
    order_start_date = models.DateTimeField()
    order_end_date = models.DateTimeField()
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('machine', 'order_start_date')
