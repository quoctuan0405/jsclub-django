from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.http import Http404
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Confession
from comment.models import Comment
# Create your views here.

def home(request):
	confessions = Confession.objects.all().order_by('-pub_date')
	return render(request, 'confession/home.html', {"confessions": confessions})

@login_required
def create(request):
	if request.method == 'POST':
		if request.POST['title'] and request.POST['body']:
			newconf = Confession()
			newconf.title = request.POST['title']
			newconf.body = request.POST['body']
			newconf.pub_date = timezone.datetime.now()
			try:
				if request.POST['anonymous']:
					newconf.author = User.objects.get(pk=1)
			except:
				newconf.author = request.user
			newconf.save()
			return redirect('detailconfession', newconf.pk) #NOT DONE YET
		else:
			return render(request, 'confession/create.html', {'error': 'Please fill all the fields'})
	else:
		return render(request, 'confession/create.html')

def detail(request, cf_id):
	try:
		confession = Confession.objects.get(pk=cf_id)
	except Confession.DoesNotExist:
		return redirect('homeconfession') #NOT DONE YET
	comments = Comment.objects.filter(confession=confession)
	if request.method == 'GET':
		return render(request, 'confession/details.html', {'confession': confession, 'comments': comments})
	elif request.method == 'POST':
		if request.POST['text']:
			newcomment = Comment()
			newcomment.text = request.POST['text']
			newcomment.pub_date = timezone.datetime.now()
			newcomment.author = request.user
			newcomment.confession = Confession.objects.get(pk=cf_id)
			newcomment.save()
			return redirect('detailconfession', confession.pk)
		else:
			return render(request, 'confession/details.html', {'confession': confession, 'error': 'You can\'t leave a blank comment', 'comments': comments})