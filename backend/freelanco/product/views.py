from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Item, OrderItem, Order
import logging

logger = logging.getLogger(__name__)

def item_list(request):
	items = Item.objects.all()
	if items.exists():
		context = {
			'items': items,
			'items_exist': True
		}
	else:
		context = {
			'items_exist': False
		}
	return render(request, "services_temp/service_providers.html", context)

def display_cart_items(request):
	order_objects = Order.objects.filter(user=request.user.customer_profile , ordered = False)
	if order_objects.exists():
		items = order_objects[0].items
		context = {
			'cart_items': items,
			'items_exist': True
		}
	else:
		context = {
			'items_exist': False
		}
	return render(request, "services_temp/cart.html", context)

def old_orders(request):
	# This will give a list of orders that are now history
	order_objects = Order.objects.filter(user=request.user.customer_profile , ordered = True)
	if order_objects.exists():
		context={
			'order_exists':True,
			'orders':order_objects
		}
	else:
		context = {
			'order_exists':False
		}
	return render(request, "base.html", context)

# Add item
@login_required
def add_to_cart(request, slug):

	item = get_object_or_404(Item, slug=slug)
	orderItem, created = OrderItem.objects.get_or_create(
		item = item,
		user = request.user.customer_profile,
		ordered = False
	)

	cart = Order.objects.filter(user = request.user.customer_profile, ordered=False)
	if cart.exists():
		cart = cart[0]
		if cart.items.filter(item = item).exists():
			pass
		else:
			cart.items.add(orderItem)
	else:
		cart = Order.objects.create( user = request.user.customer_profile )
		cart.items.add(orderItem)
	
	return redirect("item list")

# Delete item
@login_required
def remove_from_cart(request,slug):
	item = get_object_or_404(Item, slug=slug)

	cart = Order.objects.filter(user = request.user.customer_profile, ordered=False)
	if cart.exists():
		cart = cart[0]
		if cart.items.filter(item_slug = slug).exists():
			orderItem = OrderItem.objects.filter(
											user = request.user.customer_profile,
											item = item
											)[0]
			cart.items.remove(orderItem)
		else:
			messages.info("This item wasn't present in your cart.")
	else:
		messages.info("You don't have an ongoing order.")

# Item detail view
def detail_view(request, slug):
	item = get_object_or_404(Item, slug = slug)

	context = {
		'item': item,
		'provider': item.provider
	}

	return render(request, 'base.html', context)


# Place order - Need to work on this
# Add notifications feature in this feature