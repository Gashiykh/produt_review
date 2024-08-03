from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.shortcuts import get_object_or_404


from webapp.models import Review
from webapp.forms import ReviewForm


class ReviewListView(generic.ListView):
    model = Review
    template_name = 'products/detail.html'
    context_object_name = 'reviews'


class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'

    def form_valid(self, form):
        form.instance.product_id = self.kwargs['product_id']
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        return reverse_lazy('products_detail', kwargs={'id': self.kwargs['product_id']})
    

class ReviewUpdateView(PermissionRequiredMixin, generic.UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/review.html'
    pk_url_kwarg = 'id'
    permission_required = 'webapp.change_review'

    def has_permission(self) -> bool:
        review = self.get_object()
        return super().has_permission() or self.request.user == review.author

    def get_success_url(self) -> str:
        return reverse_lazy('products_detail', kwargs={'id': self.kwargs['product_id']})
    

class ReviewDeleteView(PermissionRequiredMixin, generic.DeleteView):
    model = Review
    pk_url_kwarg = 'id'
    permission_required = 'webapp.delete_review'

    def has_permission(self) -> bool:
        review = self.get_object()
        return super().has_permission() or self.request.user == review.author

    def get_success_url(self) -> str:
        return reverse_lazy('products_detail', kwargs={'id': self.kwargs['product_id']})