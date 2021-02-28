from django.shortcuts import render
from .models import PhoneBook

from django.core.paginator import Paginator
from django.db.models import Q
# Create your views here.

def main(request):
	seach_query =  request.GET.get('search', '')
	if seach_query:
		data = PhoneBook.objects.filter(Q(name__icontains=seach_query) | Q(phone__icontains=seach_query))

	else:
		data = PhoneBook.objects.all()

	paginator = Paginator(data, 2)
	page_number = request.GET.get('page', 1)
	page = paginator.get_page(page_number)

	is_paginated = page.has_other_pages()

	if page.has_previous():
		prev_url = f'?page={page.previous_page_number()}'
	else:
		prev_url = ''
	if page.has_next():
		next_url = f'?page={page.next_page_number()}'
	else:
		next_url = ''

	context = {
		'page_object': page,
		'is_paginated': is_paginated,
		'next_url': next_url,
		'prev_url': prev_url
	}

	return render(request, 'index.html', context=context)


