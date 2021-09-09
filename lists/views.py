from django.shortcuts import redirect, render

from lists.models import Item


def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    else:
        new_item_text = ''

    return render(request, 'home.html', {'items': Item.objects.all()})
