from django.urls import reverse
import pytest
from products.models import Category

@pytest.mark.django_db()
def test_view_all_products(client, create_categories_and_subcategories, login_user):
    category_name, description, _ = create_categories_and_subcategories
    response = client.get(reverse('all-products'))
    cat_name = [category.category_name for category in response.context['categories']]
    cat_description = [category.category_description for category in response.context['categories']]
    
    assert len(response.context['categories']) == 1
    assert list(response.context['categories']) == list(Category.objects.all())
    assert category_name in cat_name
    assert description in cat_description
    assert response.context['cart_count'] == 0
 

