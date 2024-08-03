from django.views import generic

from webapp.views.product import (
    ProductListView,
    ProductDetailView,
    ProductCreateView,
    ProductUpdateView,
    ProductDeleteView
)

from webapp.views.review import (
    ReviewCreateView,
    ReviewUpdateView,
    ReviewDeleteView
)

class RedirectView(generic.RedirectView):
    pattern_name = 'products'