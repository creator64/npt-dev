class Feature:
    def __init__(self, title, description, icon="fab fa-python"):
        self.icon = icon
        self.title = title
        self.description = description
        self.it = {"icon": self.icon, "title": self.title, "description": self.description}
    
    def __iter__(self):
        return iter(self.it)

f1 = Feature('Garantie',
			'''De tapijten die NPT verkoopt zijn gegarandeerd handgeknoopt en van excellente kwaliteit. 
			   Daarom ontvangt iedere koper een Certificaat van Echtheid en een garantie van 2 jaar bij normaal gebruik.''',
			   icon="fas fa-clock")


f2 = Feature('Advies',
			'''Het bedrijf NPT van de familie Ayar selecteert al sinds 1974 de hoogste kwaliteit Perzische tapijten uit het hele gebied tussen China en Noord Afrika. 
			Zelf met Iraanse wortels, heeft de familie een grote kennis van tapijten voor zowel kleine als grote interieurs. 
			Ayar adviseeert niet alleen over geschikte formaten maar ook over dessins die passen bij uw interieur. 
			Bovendien kunt u een tapijt gratis een maand uitproberen.''',
			 icon="fas fa-hands-helping")

f3 = Feature('Gratis Thuis Proberen', 
			'''Als u in onze winkel een tapijt ziet dat u mooi vindt, maar u weet niet of het ook in uw interieur goed tot zijn recht komt, 
			   kunt u het in uw huis of kantoor uitproberen.'''
			   #Wij brengen hiervoor alleen de transportkosten voor het halen en brengen in rekening als u besluit het tapijt niet te kopen. 
			   #Als u het tapijt definitief aankoopt worden de door u betaalde bezorgkosten in mindering gebracht.''',
			   ,icon="fas fa-home")

f4 = Feature('Een Lange Termijn',
			'''Bij NPT hoeft u geen zorgen te maken waarmee u over 20 jaar uw huis mee decoreert. 
			Want vanwege de slijtvastheid van onze tapijten gaan ze wel meer dan 100 jaar mee!''',
			icon="fas fa-euro-sign")


featurelist = [f1, f4, f3]