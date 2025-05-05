from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Order, Campaign, Comment
from .forms import OrderForm

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')

    def test_user_creation(self):
        self.assertEqual(self.user.username, 'testuser')
        self.assertTrue(self.user.check_password('testpass'))

class OrderModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='orderuser', password='pass')
        self.order = Order.objects.create(
            owner=self.user,
            order_Email='test@example.com',
            order_company_name='Test Co',
            order_Number='12345'
        )

    def test_order_str(self):
        self.assertIn('Test Co', str(self.order))

class OrderViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='viewuser', password='pass')
        self.order = Order.objects.create(
            owner=self.user,
            order_Email='view@example.com',
            order_company_name='View Co',
            order_Number='54321'
        )

    def test_orders_list_view_requires_login(self):
        response = self.client.get(reverse('crm:OrdersListView'))
        self.assertNotEqual(response.status_code, 200)  # Should redirect to login

    def test_orders_list_view_logged_in(self):
        self.client.login(username='viewuser', password='pass')
        response = self.client.get(reverse('crm:OrdersListView'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'View Co')

class OrderFormTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='formuser', password='pass')
        self.campaign = Campaign.objects.create(name='Test Campaign')  # Adjust if your Campaign model needs more fields

    def test_valid_form(self):
        data = {
            'status': Order.Status.new,  # Use a valid status value
            'campaign': self.campaign.pk,
            'order_Mobile': '07123456789',
            'order_connection_type': 'New',  # Use a valid choice
            'order_Title': 'Mr',  # Use a valid title
            'order_company_name': 'Form Co',
            'order_company_type': 'Ltd',  # Use a valid company type
            'order_First_Name': 'John',
            'order_Last_Name': 'Doe',
            'order_Landline': '0123456789',
            'order_Email': 'form@example.com',
            'order_date_of_birth': '1990-01-01',
            'order_House_Number': '1',
            'order_Street': 'Main St',
            'order_City': 'London',
            'order_County': 'Greater London',
            'order_Postcode': 'E1 6AN',
            'order_Delivery_House_Number': '1',
            'order_Delivery_Street': 'Main St',
            'order_Delivery_City': 'London',
            'order_Delivery_County': 'Greater London',
            'order_Delivery_Postcode': 'E1 6AN',
            'order_network': 'O2',  # Use a valid network
            'order_tariff': 'Standard',  # Use a valid tariff
            'order_eligibility_date': '2024-01-01',
            'order_box_value': 100,
            'order_spend_cap': 10,
            'order_sim_required': True,
            'order_commission_details': '10%',
            'order_additional_details': 'None',
            # Add any other required fields here
        }
        form = OrderForm(data)
        print(form.errors)  # This will help you see if any fields are missing or invalid
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = OrderForm({})
        self.assertFalse(form.is_valid())
