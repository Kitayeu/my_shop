from django.shortcuts import render, get_object_or_404, redirect

from .models import Category, Product, Review
from .forms import ReviewForm


def product_list(request, category_slug=None):
    categories = Category.objects.all()
    if category_slug:
        request_category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=request_category)
    else:
        request_category = None
        products = Product.objects.all()

    return render(request, 'shops/product/list.html',
                  {'request_category': request_category,
                   'categories': categories,
                   'products': products})


def product_detail(request, category_slug, product_slug):
    category = get_object_or_404(Category, slug=category_slug)
    product = get_object_or_404(Product, category_id=category.id, slug=product_slug)

    if request.method == 'POST':
        review_form = ReviewForm(request.POST)
        if review_form.is_valid():
            cf = review_form.cleaned_data
            author_name = 'Anonymous'
            Review.objects.create(product=product, author=author_name, text=cf['text'], rating=cf['rating'])
        return redirect('shops:product_detail', category_slug=category_slug, product_slug=product_slug)
    else:
        review_form = ReviewForm()

    return render(request, 'shops/product/detail.html',
                  {'category': category,
                   'product': product,
                   'review_form': review_form})
