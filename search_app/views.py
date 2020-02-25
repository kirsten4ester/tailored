from django.shortcuts import render
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from tailored.models import Category


def is_valid_queryparam(param):
    return param != '' and param is not None

@login_required
def photographer_search(request):
    qs = Category.objects.all()
    category = Category.objects.all()
    location_contains_query = request.GET.get('location_contains')
    category = request.GET.get('category')
    price = request.GET.get('price')

    if is_valid_queryparam(location_contains_query):
        qs = qs.filter(location__icontains=location_contains_query)
    if is_valid_queryparam(category) and category != 'Choose...':
        qs = qs.filter(category__name=category)
    if is_valid_queryparam(price) and price != 'Choose...':
        qs = qs.filter(price__name=price)

    context = {
        'queryset': qs,
        'category': category,
        'price': price,
    }
    return render(request, "search_app/photographer_search.html", context)