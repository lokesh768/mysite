from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from .forms import ItemForm
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required

def Welcome(request):
    return render(request, 'food/welcome.html')

@login_required()
def index(request):
    item_list = Item.objects.all()
    context = {
        'item_list':item_list,
    }
    return render(request, 'food/index.html', context)


# this is class based view for detailing each item
class Detail(DetailView):
    model = Item
    template_name = 'food/detail.html'


# this is class based view for create item
class CreateItem(CreateView):
    model = Item
    fields = ['item_name', 'item_description', 'item_price', 'item_image']
    template_name = 'food/item-form.html'
    def form_valid(self,form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)
    
@login_required()
def update_item(request, id):
    item = Item.objects.get(id=id)
    form = ItemForm(request.POST or None, instance=item)
    if form.is_valid():
        form.save()
        return redirect('food:index')
    return render(request, 'food/item-form.html', {'form':form, 'item':item })

@login_required()
def delete_item(request, id):
    item = Item.objects.get(id=id)
    
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item':item})