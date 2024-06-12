from django.urls import reverse
import pytest

@pytest.mark.django_db()
def test_view_all_products(client, create_categories_and_subcategories):
    category, description, subcategory = create_categories_and_subcategories
    response = client.get(reverse('all-products'))
    assert response.context['categories'].category_name == category


