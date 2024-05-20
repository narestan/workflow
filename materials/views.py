# materials/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import CategoryItem, Item
from .forms import CategoryItemForm, ItemForm

def category_list(request):
    categories = CategoryItem.objects.all()
    return render(request, 'materials/category_list.html', {'categories': categories})

def category_create(request):
    if request.method == 'POST':
        form = CategoryItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('materials:category_list')
    else:
        form = CategoryItemForm()
    return render(request, 'materials/category_form.html', {'form': form})

def item_list(request, category_id):
    category = get_object_or_404(CategoryItem, id=category_id)
    items = Item.objects.filter(category=category)
    return render(request, 'materials/item_list.html', {'category': category, 'items': items})

def item_create(request, category_id):
    category = get_object_or_404(CategoryItem, id=category_id)
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.category = category
            item.save()
            return redirect('materials:item_list', category_id=category.id)
    else:
        form = ItemForm(initial={'category': category})
    return render(request, 'materials/item_form.html', {'form': form, 'category': category})
