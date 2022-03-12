from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from npt.settings import EMAIL_HOST_USER
from .assets.feature import featurelist
from .assets.faq import flist

# Create your views here.

def home(response):
	return render(response, "main/home.html", {"actdict": {"home": "active"}, "features": featurelist}) 

def contact(response):
	data = response.POST
	print("info: ", data, bool(data))

	if bool(data):
		#send the email
		sender_email = "<" + data["email"] + ">"
		subject = data["subject"]
		message = data["message"]

		sent_mail = send_mail(subject,
				  message,
				  sender_email,
				  [EMAIL_HOST_USER],
				  fail_silently=True)

		if bool(sent_mail):
			state = "success"
		else:
			state = "failure"

		return render(response, "main/contact.html", {"actdict": {"contact": "active"}, "state": state}) 
	else:
		return render(response, "main/contact.html", {"actdict": {"contact": "active"}}) 

def about(response):
	return render(response, "main/about.html", {"actdict": {"about": "active"}}) 

def faq(response):
	return render(response, "main/faq.html", {"actdict": {"faq": "active"}, "flist": flist, })