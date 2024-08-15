from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    national_id = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class BankAccount(models.Model):
    owner = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='accounts')
    account_id = models.CharField(max_length=20, unique=True)
    balance = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return f"Account {self.account_id} - Owner: {self.owner}"

