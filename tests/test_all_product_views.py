from django.urls import reverse
import pytest
from products.models import Category

@pytest.mark.django_db()
def test_view_all_products(client, create_categories_and_subcategories, mocker):
    category_name, description, _ = create_categories_and_subcategories
    response = client.get(reverse('all-products'))
    cat_name = [category.category_name for category in response.context['categories']]
    cat_description = [category.category_description for category in response.context['categories']]
    cart_count = mocker.patch('basket.basket.NavBar_Basket_count')
    cart_count = cart_count.return_value
    cart_count.calculate.return_value == 5

    assert len(response.context['categories']) == 1
    assert list(response.context['categories']) == list(Category.objects.all())
    assert category_name in cat_name
    assert description in cat_description
    # assert response.context['cart_count'] == 5
    print(response.context)

