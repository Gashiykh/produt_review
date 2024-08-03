from django.urls import path

from webapp import views

urlpatterns = [
    path('', views.RedirectView.as_view(), name='redirect'),
    path('products', views.ProductListView.as_view(), name='products'),
    path('products/add', views.ProductCreateView.as_view(), name='products_add'),
    path('products/<int:id>', views.ProductDetailView.as_view(), name='products_detail'),
    path('products/<int:id>/update', views.ProductUpdateView.as_view(), name='products_update'),
    path('products/<int:id>/delete', views.ProductDeleteView.as_view(), name='products_delete'),
    path('products/<int:product_id>/review/add', views.ReviewCreateView.as_view(), name='reviews_add'),
    path('products/<int:product_id>/review/<int:id>/update', views.ReviewUpdateView.as_view(), name='reviews_update'),
    path('products/<int:product_id>/review/<int:id>/delete', views.ReviewDeleteView.as_view(), name='reviews_delete'),
]