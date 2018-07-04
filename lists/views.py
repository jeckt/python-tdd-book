from django.shortcuts import redirect, render

from lists.models import Item

# TODO(steve): Display multiple items in the table
# TODO(steve): Support more than one list!
def home_page(request):
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
