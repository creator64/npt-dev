from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from npt.settings import EMAIL_HOST_USER
from .feature import Feature

# feature objects (home)

f1 = Feature('Probeer Thuis', 
			'''Als u in onze winkel een tapijt ziet dat u mooi vindt, maar u weet niet of het ook in uw interieur goed tot zijn recht komt, 
			kunt u het een maand op proef in uw huis of kantoor uitproberen. ''',
			#Wij brengen hiervoor alleen de transportkosten voor het halen en brengen in rekening als u besluit het tapijt niet te kopen.''' 
			#Als u het tapijt definitief aankoopt worden de door u betaalde bezorgkosten in mindering genbracht.''',
			   icon="fas fa-home")

f2 = Feature('Garantie',
			'''De tapijten die NPT verkoopt zijn gegarandeerd handgeknoopt en van excellente kwaliteit. 
			   Daarom wordt een garantie van (x) jaar gegeven op ieder tapijt dat NPT levert.''',
			   icon="fas fa-exchange-alt")


f3 = Feature('Advies',
			'''Het bedrijf NPT van de familie Ayar selecteert al sinds 1974 de hoogste kwaliteit Perzische tapijten uit het gebied tussen Afghanistan en Turkije. 
			Zelf met Iraanse wortels, heeft de familie een grote kennis van tapijten voor zowel kleine als grote interieurs. 
			Ayar adviseeert niet alleen over geschikte formaten maar ook over dessins die passen bij uw interieur.''',
			#Bovendien kunt u een tapijt gratis een maand uitproberen.''',
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