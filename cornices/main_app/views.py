from django.shortcuts import render
from django.views.generic import ListView, View

from .models import Contact, PriceList


class ContactsPageView(ListView):
    model = Contact
    template_name = 'contacts.html'


class HomePageView(View):
    def get(self, request):
        return render(request, 'home_page.html')


class PriceListPageView(ListView):
    model = PriceList
    template_name = 'price_list.html'
