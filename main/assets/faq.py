class Faq:
    idn = 0
    def __init__(self, q, a="blabla"*10, qtype="a"):
        self.q = q
        self.a = a 
        self.qtype = qtype
        self.id = self.__class__.idn
        self.__class__.idn += 1


f1 = Faq("Hoe herken je een handgeknoopt tapijt?")
f2 = Faq("Wanneer werd de eerste tapijt gebruikt?")
f3 = Faq("Waarom zijn Perzische tapijten zo duur?")
f4 = Faq("Past een Oosters Tapijt in een modern interieur?")
f5 = Faq("Hoe worden handgeknoopte tapijten gemaakt?")
f6 = Faq("Wat is de pool van een tapijt?")
f7 = Faq("Hoelang duurt het om een tapijt te maken?")

flist = [f1, f2, f3, f4, f5, f6, f7]