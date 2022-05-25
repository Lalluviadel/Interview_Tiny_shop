from django.views.generic import ListView

from products.models import Product


class ProductsView(ListView):
    model = Product
    template_name = 'products/goods_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Добро пожаловать'
        context['products'] = Product.objects.all()
        return context
