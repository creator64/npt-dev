from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail
from npt.settings import EMAIL_HOST_USER
from .feature import Feature

# feature objects (home)

f1 = Feature('Garantie',
			'''De tapijten die NPT verkoopt zijn gegarandeerd handgeknoopt en van excellente kwaliteit. 
			   Daarom ontvangt iedere koper een Certificaat van Echtheid en een garantie van 2 jaar bij normaal gebruik.
			   Reclames binnen twee maanden.''',
			   icon="fas fa-clock")


f2 = Feature('Advies',
			'''Het bedrijf NPT van de familie Ayar selecteert al sinds 1974 de hoogste kwaliteit Perzische tapijten uit het hele gebied tussen China en Noord Afrika. 
			Zelf met Iraanse wortels, heeft de familie een grote kennis van tapijten voor zowel kleine als grote interieurs. 
			Ayar adviseeert niet alleen over geschikte formaten maar ook over dessins die passen bij uw interieur. 
			Bovendien kunt u een tapijt gratis een maand uitproberen.''',
			 icon="fas fa-hands-helping")

f3 = Feature('Gratis Thuis Proberen', 
			'''Als u in onze winkel een tapijt ziet dat u mooi vindt, maar u weet niet of het ook in uw interieur goed tot zijn recht komt, 
			   kunt u het op proef in uw huis of kantoor uitproberen.'''
			   #Wij brengen hiervoor alleen de transportkosten voor het halen en brengen in rekening als u besluit het tapijt niet te kopen. 
			   #Als u het tapijt definitief aankoopt worden de door u betaalde bezorgkosten in mindering gebracht.''',
			   ,icon="fas fa-home")

f4 = Feature('Een Lange Termijn',
			'''Bij NPT hoeft u geen zorgen te maken waarmee u over 20 jaar uw huis mee decoreert. 
			Want vanwege de slijtvastheid van onze tapijten gaan ze wel meer dan 100 jaar mee!''',
			icon="fas fa-euro-sign")

# Create your views here.

def home(response):
	return render(response, "main/home.html", {"actdict": {"home": "active"}, "features": [f1, f4, f3]}) 

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
	return render(response, "main/faq.html", {"actdict": {"faq": "active"}})