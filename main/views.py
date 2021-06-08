from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from npt.settings import EMAIL_HOST_USER
from .feature import Feature

# feature objects (home)

f1 = Feature('Probeer Thuis', 
			'''Bij NPT kunt u tapijten die u mooi vindt eerst zelf mee naar huis nemen en uitproberen voordat u ze koopt. 
               In de huiskamer kunnen ze er anders uitzien dan in de winkel''',
			   icon="fas fa-home")

f2 = Feature('Inruilen Mogelijk',
			'''Heeft u zelf tapijten waar u van af wil? Dat komt mooi uit.
               Bij NPT kunt u uw oude tapijten inruilen en flinke korting krijgen op een nieuwe''',
			   icon="fas fa-exchange-alt")


f3 = Feature('Advies',
			'''Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu
             fugiat nulla pariatur trade stravi''',
			 icon="fas fa-hands-helping")

# Create your views here.

def home(response):
	return render(response, "main/home.html", {"actdict": {"home": "active"}, "features": [f1, f2, f3]}) 

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