from django.shortcuts import render, redirect
from time import gmtime, strftime
import random

# Create your views here.
def index(request):
    if 'my_gold' and 'gold_earned' and 'log' not in request.session:
        request.session['my_gold'] = 0
        request.session['gold_earned'] = 0
        request.session['log'] = []

    return render(request, 'gold/index.html')

def farm(request):

    request.session['gold_earned'] = random.randint(10, 21)

    request.session['my_gold'] += request.session['gold_earned']

    context = {
        'gold': request.session['gold_earned'],
        'time': strftime('%Y-%m-%d %H:%M %p', gmtime()),
        'location': 'farm'
    }

    datalist = request.session['log']
    datalist.append(context)
    request.session['log'] = datalist

    return redirect('/')

def cave(request):
    request.session['gold_earned'] = random.randint(5, 11)

    request.session['my_gold'] += request.session['gold_earned']

    context = {
        'gold': request.session['gold_earned'],
        'time': strftime('%Y-%m-%d %H:%M %p', gmtime()),
        'location': 'cave'
    }

    datalist = request.session['log']
    datalist.append(context)
    request.session['log'] = datalist

    return redirect('/')

def house(request):
    request.session['gold_earned'] = random.randint(2, 5)

    request.session['my_gold'] += request.session['gold_earned']

    context = {
        'gold': request.session['gold_earned'],
        'time': strftime('%Y-%m-%d %H:%M %p', gmtime()),
        'location': 'house'
    }

    datalist = request.session['log']
    datalist.append(context)
    request.session['log'] = datalist

    return redirect('/')

def casino(request):
    request.session['gold_earned'] = random.randint(-50, 51)

    request.session['my_gold'] += request.session['gold_earned']

    context = {
        'gold': request.session['gold_earned'],
        'time': strftime('%Y-%m-%d %H:%M %p', gmtime()),
        'location': 'casino'
    }

    datalist = request.session['log']
    datalist.append(context)
    request.session['log'] = datalist

    return redirect('/')

def reset(request):
    request.session.clear()
    return redirect('/')