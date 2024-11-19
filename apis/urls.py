from django.urls import path
from .views import *
urlpatterns = [
    # Customer 
    path('customers/', CustomerListCreateView.as_view(), name='customer-list-create'),
    path('createcustomer',CreateCustomerAPIView.as_view(),name='create-customer'),
    path('customers/<int:pk>/', CustomerDetailView.as_view(), name='customer-detail'),

    # Wallet 
    path('wallets/', WalletListCreateView.as_view(), name='wallet-list-create'),
    path('wallets/<int:pk>/', WalletDetailView.as_view(), name='wallet-detail'),
    path('createwallet',CreateWalletAPIView.as_view(),name='create-wallet'),
    
    # Loan 
    path('loans/', LoanListCreateView.as_view(), name='loan-list-create'),
    path('loans/<int:pk>/', LoanDetailView.as_view(), name='loan-detail'),
    path('createloan',LoanListCreateView.as_view(),name='create-loan'),

    # Payment 
    path('payments/', PaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', PaymentDetailView.as_view(), name='payment-detail'),
    path('createpayment',CreatePaymentAPIView.as_view(),name='create-payment'),

]
