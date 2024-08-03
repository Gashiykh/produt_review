from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin

from webapp.models import Product
from webapp.forms import ProductForm, ReviewForm


class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/list.html'
    context_object_name = 'products'
    

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/detail.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = self.object.reviews.all()
        context['review_form'] = ReviewForm()
        return context

class ProductCreateView(PermissionRequiredMixin, generic.CreateView):
    model = Product
    template_name = 'products/product.html'
    form_class = ProductForm
    permission_required = 'webapp.add_product'

    def get_success_url(self) -> str:
        return reverse('products_detail', kwargs={'id': self.object.id})
    

class ProductUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Product
    template_name = 'products/product.html'
    form_class = ProductForm
    pk_url_kwarg = 'id'
    permission_required = 'webapp.update_product'

    def get_success_url(self) -> str:
        return reverse('products_detail', kwargs={'id': self.object.id})
    

class ProductDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Product
    pk_url_kwarg = 'id'
    permission_required = 'webapp.delete_product'

    def get_success_url(self) -> str:
        return reverse_lazy('products')