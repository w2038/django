from django.shortcuts import render, HttpResponse

# Create your views here.

def hello(request, nome, number, number2):
    return HttpResponse(f'Hello {nome}, a soma dos número é {number+number2}')

def multiplicacao(request, number, number2):
    return HttpResponse(f'A multiplicacao dos numeros são {number*number2}')

def divisao(request, number, number2):
    return HttpResponse(f'A divisao dos numeros são {number/number2}')

def subtracao(request, number, number2):
    return HttpResponse(f'A subtracao dos numeros são {number-number2}')