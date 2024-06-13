from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed
from products.models import Category, Product, ProductType

@pytest.mark.django_db()
def test_view_all_products(client, create_categories_and_subcategories, create_product):
    category_name, description, _, _ = create_categories_and_subcategories
    response = client.get(reverse('all-products'))
    cat_name = [category.category_name for category in response.context['categories']]
    cat_description = [category.category_description for category in response.context['categories']]
    product_titles = [product.product_title for category in response.context['categories'] for product in category.product_categories.all()]
    
    assert len(response.context['categories']) == 1
    assert list(response.context['categories']) == list(Category.objects.all())
    assert category_name in cat_name
    assert description in cat_description
    assert response.context['cart_count'] == None
    assert product_titles == ['noodless', 'cat']
    assert response.status_code == 200
    assertTemplateUsed(response, "products/all-products.html")


