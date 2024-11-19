from rest_framework import serializers
from .models import *
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'user', 'phone', 'email', 'created_at']

class WalletSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Wallet
        fields = ['id', 'customer', 'balance']

    def to_representation(self, instance):
        data = super().to_representation(instance)

        if instance.customer:  
            data['customer'] = {
                'id': instance.customer.id,  
                'name': instance.customer.name  
            }

        return data


class LoanSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Loan
        fields = ['id', 'customer', 'user', 'total_amount', 'description', 'duration', 'is_paid', 'remaining_amount', 'created_at']
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        if instance.user: 
            data['user'] = {
                'id': instance.user.id, 
                'username': instance.user.username  
            }
        return data

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id', 'loan', 'amount', 'payment_date', 'description']
