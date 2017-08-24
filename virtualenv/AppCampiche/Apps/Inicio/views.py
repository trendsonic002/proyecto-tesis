# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import Administrador
from .forms import formLog

def index(request):
	return render_to_response('Inicio/index.html');

def iniciar_sesion(request):
	if request.method == 'POST':
		formulario = formLog(request.POST)
		if formulario.is_valid:
			usuario = request.POST['usuario']
			clave = request.POST['password']

			verificacion = Administrador.objects.filter(usuario=usuario,contrasenia=clave).exists()
			print (verificacion)

			if verificacion == True:
				return HttpResponseRedirect('www.google.cl')
			else:
				return HttpResponseRedirect('www.youtube.com')

	else:
		formulario = formLog()
	context = {'formulario':formulario}
	return render(request,'inicio/index.html',context)

