from rest_framework import serializers
from .models import Invoices, InvoicesDetails

class InvoiceSerializer(serializers.ModelSerializer):
    # invoice_details = InvoiceDetailSerializer(many=True, read_only=True)
    class Meta:
        model = Invoices
        fields = '__all__'

class InvoiceDetailSerializer(serializers.ModelSerializer):
    # invoices = InvoiceSerializer(read_only=True)
    class Meta:
        model = InvoicesDetails
        fields = '__all__'



