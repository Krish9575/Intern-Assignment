from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoices, InvoicesDetails


class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.invoice_data = {"Date": "2024-01-10", "CustomerName": "Test Customer"}
        self.invoice = Invoices.objects.create(**self.invoice_data)

    def test_delete_invoice(self):
        response = self.client.delete(f'/url/invoices/{int(self.invoice.id)}/')
        print("Delete :",self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT))

    def test_get_invoice_detail(self):
        response = self.client.get(f'/url/invoices/{int(self.invoice.id)}/')
        print("Get :",self.assertEqual(response.status_code, status.HTTP_200_OK))

    def test_partial_update_invoice(self):
        partial_data = {"Date": "2024-01-12"}
        response = self.client.patch(f'/url/invoices/{int(self.invoice.id)}/', partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_invoice(self):
        updated_data = {"Date": "2024-01-15", "CustomerName": "Updated Customer"}
        response = self.client.put(f'/url/invoices/{int(self.invoice.id)}/', updated_data, format='json')
        print("Update :", self.assertEqual(response.status_code, status.HTTP_200_OK))

class InvoiceDetailsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create an Invoices instance
        self.invoice_data = {"Date": "2024-01-10", "CustomerName": "Test Customer"}
        self.invoice = Invoices.objects.create(**self.invoice_data)

         # Create an InvoicesDetails instance associated with the Invoices instance
        self.invoice_details_data = {
            "invoices": self.invoice,  # Use the Invoices instance
            "description": "Test Description",
            "quantity": 5,
            "unit_price": 15.0
        }
        self.invoice_details = InvoicesDetails.objects.create(**self.invoice_details_data)

    def test_delete_invoice_details(self):
        # Ensure that the URL corresponds to the specific InvoicesDetails instance
        url = f'/url/invoicesDetails/{self.invoice_details.id}/'
        response = self.client.delete(url)

        if response.status_code != status.HTTP_204_NO_CONTENT:
            print(f"Delete request failed. URL: {url}")
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.content}")

        print("Delete :" ,self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT))

    
    def test_get_invoice_details_detail(self):
        # Ensure that the URL corresponds to the specific InvoicesDetails instance
        url = f'/url/invoicesDetails/{self.invoice_details.id}/'
        response = self.client.get(url)

        if response.status_code != status.HTTP_200_OK:
            print(f"Get request failed. URL: {url}")
            print(f"Response status code: {response.status_code}")
            print(f"Response content: {response.content}")

        print("Get :",self.assertEqual(response.status_code, status.HTTP_200_OK))


    

    def test_partial_update_invoice_details(self):
        invoice_details = InvoicesDetails.objects.create(**self.invoice_details_data)
        partial_data = {"quantity": 8}
        response = self.client.patch(f'/url/invoicesDetails/{int(invoice_details.id)}/', partial_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        
    def test_update_invoice_details(self):
        # Ensure that the URL corresponds to the specific InvoicesDetails instance
        url = f'/url/invoicesDetails/{self.invoice_details.id}/'
       
        updated_data = {
            "invoices":self.invoice.id,
            "description": "Updated Description",
            "quantity": 10,
            "unit_price": 20.0
        }

        # # Send the PUT request
        response = self.client.put(url, data=updated_data, format='json')
        # # Assert the response status code
        
        print("Update : ",self.assertEqual(response.status_code, status.HTTP_200_OK))
      
