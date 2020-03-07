from django.shortcuts import render, redirect
from .models import Comment
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from confession.models import Confession

# Create your views here.

def view(request, cf_id):
	comments = Comment.objects.filter(confession=cf_id)
	return render(request, 'comment/view.html', {"comments":comments, "confessionid":cf_id})

@login_required
def create(request, cf_id):
	if request.method == 'POST':
		if request.POST['text']:
			newconf = Comment()
			newconf.text = request.POST['text']
			newconf.pub_date = timezone.datetime.now()
			newconf.author = request.user
			newconf.confession = Confession.objects.get(pk=cf_id)
			newconf.save()
			return redirect('viewcomment', cf_id)
		else:
			return render(request, 'comment/create.html', {'error': 'Please fill all the fields'})
	else:
		return render(request, 'comment/create.html', {"confessionid":cf_id})