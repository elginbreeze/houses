from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

def index(request):
	context = {}
	return render(request, 'calculator/calculate.html', context)

def calculate(request):
	try:
		pprice = float( request.POST.get('purchasePrice','') )
		down   = float( request.POST.get('downPayment','') )
		mort   = int( request.POST.get('mortgageTerm','') )
		intRt  = float( request.POST.get('interestRate','') )
		insur  = float( request.POST.get('insurance','') )
		pmi    = request.POST.get('pmi','')
		fstPay = request.POST.get('firstPayment','')

		remainder = pprice - down
	except:
		return 'error'

	return 'error'

def results( request ):
	results = calculate( request )
	context = {}
	if isinstance( results, str ):
		messages.error(request, "Error")
		print 'Error'
	else:
		print pprice
		context[ 'vars' ] = pprice

	return render( request, 'calculator/calculate.html', context )