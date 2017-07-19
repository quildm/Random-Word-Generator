from django.shortcuts import render, HttpResponse, redirect
import random, string

x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(14))


def index(request):
	response = "Random word "+ x
	print(x)

	return HttpResponse(response)