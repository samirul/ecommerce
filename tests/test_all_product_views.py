from django.urls import reverse
import pytest

@pytest.mark.django_db()
def test_view_all_products(client):
    response = client.get(reverse('all-products'))
    print(response.context)


