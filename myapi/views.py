from django.shortcuts import render

# Create your views here.

from .models import Stock
from django.http import HttpResponse, HttpResponseBadRequest


def getAll(req):
    people = Stock.objects.all().values("type", "amount")
    return HttpResponse(people, content_type='application/json')


def getSum(req):
    queryset = Stock.objects.all().order_by('id')
    stock = 0
    for obj in queryset:
        stock += obj.amount
    return HttpResponse(stock)

def buyOne(req, id):
    queryset = Stock.objects.filter(id=id).values_list('amount').first()
    if not queryset:
        return HttpResponseBadRequest('No product under this id')
    amount = list(queryset)
    list_amount = amount[0]
    if list_amount == 0:
        return HttpResponseBadRequest('Sold out')
    else:
        Stock.objects.filter(id=id).update(amount=list_amount - 1)
        return HttpResponse(f'OK, New stock is: {list_amount-1}')

