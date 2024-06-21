from django.urls import reverse
import pytest
from pytest_django.asserts import assertTemplateUsed
from products.models import Category, Product, ProductType

@pytest.mark.django_db()
def test_view_all_products(client, create_categories_and_subcategories, create_product_category):
    category_name, description, _, _, _ = create_categories_and_subcategories
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

@pytest.mark.django_db()
def test_view_products_view_by_only_category(client, create_categories_and_subcategories, create_product_category, get_slug):
    category_name, description, _, _, _ = create_categories_and_subcategories
    slug_categories, _ = get_slug
    response = client.get(reverse('productslugcategory', kwargs={'slug': slug_categories}))
    cat_name = [category.category_name for category in response.context['categories']]
    cat_description = [category.category_description for category in response.context['categories']]
    product_titles = [product.product_title for category in response.context['categories'] for product in category.product_categories.all()]

    filter_product_by_categories = Product.objects.filter(categories__category_name=category_name)
    filter_product_name = [product_name.product_title for product_name in filter_product_by_categories]

    assert len(response.context['categories']) == 1
    assert list(response.context['categories']) == list(Category.objects.all())
    assert category_name in cat_name
    assert description in cat_description
    assert response.context['cart_count'] == None
    assert product_titles == ['noodless', 'cat', 'Mango', 'Apple']
    assert product_titles == filter_product_name
    assert response.status_code == 200
    assertTemplateUsed(response, "products/products.html")


@pytest.mark.django_db()
def test_view_products_view_by_subcategory(client, create_categories_and_subcategories, create_product_subcategory, get_slug):
    category_name, description, subcategory_name, _, _ = create_categories_and_subcategories
    _, slug_subcategories = get_slug
    response = client.get(reverse('productslugsubcategory', kwargs={'slug': slug_subcategories}))
    cat_name = [category.category_name for category in response.context['categories']]
    cat_description = [category.category_description for category in response.context['categories']]

    filter_product_by_subcategories = Product.objects.filter(subcategories__subcategory_name=subcategory_name)
    filter_product_name = [product_name.product_title for product_name in filter_product_by_subcategories]

    assert len(response.context['categories']) == 1
    assert list(response.context['categories']) == list(Category.objects.all())
    assert category_name in cat_name
    assert description in cat_description
    assert response.context['cart_count'] == None
    assert filter_product_name == ['Mango', 'Apple']
    assert response.status_code == 200
    assertTemplateUsed(response, "products/products.html")
    