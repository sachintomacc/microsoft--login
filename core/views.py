from django.views.generic import FormView, TemplateView
from django.shortcuts import render, reverse
from .forms import *
from django.conf import settings

def home(request):
    return render(request, 'home.html')


class StripeView(TemplateView):
    template_name = "stripe-checkout.html"


# class CustomerMixin(object):
#     def get_customer(self):
#         try:
#             return self.request.user.customer
#         except:
#             Customer.create(self.request.user )


class StripeMixin(object):
    def get_context_data(self, **kwargs):
        context = super(StripeMixin, self).get_context_data(**kwargs)
        context['publishable_key'] = settings.STRIPE_PUBLIC_KEY 
        return context
    

class SuccessView(TemplateView):
    template_name = 'thankyou.html'


class SubscribeView(FormView):
    template_name = 'subscribe.html'
    form_class = StripeForm
    success_url = 'thankyou'

    def form_valid(self, form):
        pass

    def form_invalid(self, form):
        pass
