from django.views.generic import ListView

from products.models import Product, Section


class ProductsView(ListView):
    model = Product
    template_name = 'products/goods_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Добро пожаловать'
        context['categories'] = Section.objects.all()
        if self.kwargs.keys():
            context['section'] = Section.objects.get(id=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        if self.kwargs.keys():
            return Product.objects.filter(category=self.kwargs['category_id'])
        return Product.objects.all().prefetch_related('category')


class CategoryView(ListView):
    model = Product
    template_name = 'products/goods_list.html'
