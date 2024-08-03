from django.shortcuts import redirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth import get_user_model
from django.contrib.auth import login
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied

from webapp.models import Review
from accounts.forms import MyUserCreationForm, UserUpdateForm


class RegisterView(generic.CreateView):

    model = get_user_model()
    form_class = MyUserCreationForm
    template_name = 'accounts/register.html'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.get_success_url())

    def get_success_url(self):
        next_url = self.request.POST.get('next')
        
        if not next_url:
            next_url = self.request.GET.get('next')
        if not next_url:
            next_url = reverse('products')

        return next_url
    

class UserDetailView(generic.DetailView):
    model = get_user_model()
    pk_url_kwarg = 'id'
    context_object_name = 'user_obj'
    template_name = 'accounts/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_object()
        context['reviews'] = Review.objects.filter(author=user)
        return context
    

class UserUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = get_user_model()
    form_class = UserUpdateForm
    template_name = 'accounts/update.html'

    def dispatch(self, request, *args, **kwargs):
        user_obj = self.get_object()
        if request.user != user_obj:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return self.request.user
    
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('profile', kwargs={'id': self.request.user.id})
    

class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    template_name='accounts/change_password.html'
    
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
    

    def get_success_url(self) -> str:
        return reverse_lazy('profile', kwargs={'id': self.request.user.id})
    
