from django.urls import reverse
import pytest

@pytest.mark.django_db()
def test_view_all_products(client, create_categories_and_subcategories):
    category_name, description, subcategory_name = create_categories_and_subcategories
    response = client.get(reverse('all-products'))
    assert len(response.context['categories']) == 1


