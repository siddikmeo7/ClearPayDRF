from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Customer(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='wallet')
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def add_funds(self, amount):
        self.balance += amount
        self.save()

    def deduct_funds(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.save()
        else:
            raise ValueError("Not enough money in the Wallet")

    def __str__(self):
        return f"{self.customer.name} - Balance: {self.balance} TJS"


class Loan(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='loans')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    duration = models.DurationField() 
    is_paid = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def remaining_amount(self):
        total_payments = sum(payment.amount for payment in self.payments.all())
        return self.total_amount - total_payments

    def save(self, *args, **kwargs):
        if self.pk is None:  
            self.customer.wallet.add_funds(self.total_amount)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.customer.name} - {self.total_amount} TJS (Duration: {self.duration})"


class Payment(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.loan.customer.wallet.balance >= self.amount:
            self.loan.customer.wallet.deduct_funds(self.amount)
            super().save(*args, **kwargs)
        else:
            raise ValueError("Not enough money in the Wallet")

        if self.loan.remaining_amount() <= 0:
            self.loan.is_paid = True
            self.loan.save()

    def __str__(self):
        return f"Transaction {self.amount} TJS for {self.loan.customer.name}"


@receiver(post_save, sender=Customer)
def create_wallet(sender, instance, created, **kwargs):
    if created:
        wallet = Wallet.objects.create(customer=instance)
