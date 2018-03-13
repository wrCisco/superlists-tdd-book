from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

from lists.models import Item, List
from lists.forms import ExistingListItemForm, ItemForm

User = get_user_model()

# Create your views here.

def home_page(request):
    return render(request, 'lists/home.html', {'form': ItemForm()})

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)

    if request.method == 'POST':
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'lists/list.html', {'list': list_, 'form': form})
 
#         try:
#             item = Item(text=request.POST['text'], list=list_)
#             item.full_clean()
#             item.save()
#             return redirect(list_) # redirect(list_) works thanks to the get_absolute_url
#         except ValidationError:    # function defined in the List model
#             error = "You can't have an empty list item"
# 
#     form = ItemForm()
#     return render(request, 'lists/list.html', {'list': list_, 'form': form, 'error': error})

def new_list(request):
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List()
        list_.owner = request.user
        list_.save()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'lists/home.html', {'form': form})

def my_lists(request, email):
    owner = User.objects.get(email=email)
    return render(request, 'lists/my_lists.html', {'owner': owner})

