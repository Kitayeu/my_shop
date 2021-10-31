from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.postgres.search import TrigramSimilarity

from .models import Category, Product, Review
from .forms import ReviewForm, SearchForm
from carts.forms import CartAddProductForm


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
            if request.user.is_authenticated:
                author_name = request.user.first_name
                Review.objects.create(product=product, author=author_name, text=cf['text'], rating=cf['rating'])
        return redirect('shops:product_detail', category_slug=category_slug, product_slug=product_slug)
    else:
        review_form = ReviewForm()
        cart_product_form = CartAddProductForm()

    return render(request, 'shops/product/detail.html',
                  {'cart_product_form': cart_product_form,
                   'product': product,
                   'review_form': review_form})


def product_search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Product.objects.annotate(
            similarity=TrigramSimilarity('name', query),
        ).filter(similarity__gt=0.3).order_by('-similarity')
    return render(request, 'shops/product/search.html', {'form': form,
                                                         'query': query,
                                                         'results': results})
