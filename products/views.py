from django.views.generic import ListView

from products.models import Product, Section


class ProductsView(ListView):
    model = Product
    template_name = 'products/goods_list.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data()
        context['title'] = 'Добро пожаловать'
        context['site_name'] = self.request.site.name
        context['categories'] = Section.on_site.all()
        if self.kwargs.keys():
            context['section'] = Section.on_site.get(id=self.kwargs['category_id'])
        return context

    def get_queryset(self):
        if self.kwargs.keys():
            return Product.on_site.filter(category=self.kwargs['category_id'])
        return Product.on_site.all().prefetch_related('category')


class CategoryView(ListView):
    model = Product
    template_name = 'products/goods_list.html'
