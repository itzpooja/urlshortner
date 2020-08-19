from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
import hashlib
from shorten.models import UrlTable
from django.contrib.auth.models import User

# Create your views here.

def signup(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		email = request.POST.get("email")

		user = User.objects.create_user(
				username=username,
				password=password,
				email=email
			)
		login(request, user)

		return redirect("/dashboard/")

	return render(request, "signup.html")

def signin(request):
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")

		user = authenticate(username=username, password=password)

		if user != None:
			login(request, user)
			return redirect("/dashboard/")

	return render(request, "signin.html")

	
def signout(request):
	logout(request)
	return redirect("/signin/")

def dashboard(request):
	user = request.user
	works = UrlTable.objects.all()
	return render(request, "dashboard.html", {"works":works})

def create_hash(key):
	hash= hashlib.md5(key)
	return hash.hexdigest()[:6]

def create_short_url(request):
	if request.method == "POST":
		title = request.POST.get("title")
		urls= request.POST.get("long_url")
		short_url= create_hash(urls.encode('utf-8'))

		
		linking = UrlTable.objects.create(
			title=title,
			long_url=urls,
			short_hash= short_url
		)

		return redirect("/dashboard/")


def redirect_to_long_url(request,hashcode):
	url=UrlTable.objects.get(short_hash=hashcode)
	long_url=url.long_url
	print("heyyyyyyyyyyyyyyyy")
	url.no_clicks+=1
	url.save()

	return redirect(long_url)






