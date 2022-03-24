class Faq:
    idn = 0
    def __init__(self, q, a="Nog geen antwoord beschikbaar", qtype="a"):
        self.q = q
        self.a = a 
        self.qtype = qtype
        self.id = self.__class__.idn
        self.__class__.idn += 1

# Questions
f1 = Faq("Past een Oosters tapijt in een modern interieur?")
f2 = Faq("Zijn onze tapijten geschikt voor vloerverwarming?")
f3 = Faq("Zijn onze tapijten geschikt voor buiten?")
f4 = Faq("Zijn al onze tapijten handgeknoopt?")
f5 = Faq("Hoe bescherm ik mijn tapijt tegen motten?")
f6 = Faq("Waarom zijn perzische tapijten zo duur?")
f7 = Faq("Hoelang bestaan tapijten al?")
f8 = Faq("Kun je met schoenen op een tapijt lopen?")
f9 = Faq("Waar komen onze producten precies vandaan?")
f10 = Faq("Zijn er ook hoogpolige Perzische tapijen?")

flist = [f1, f6, f5, f7, f3, f8, f4, f2, f10, f9]

# Answers

f1.a = """
Wij van NPT zijn ervan overtuigd dat er bij elke interieur een Oosters tapijt past, dus ook bij een moderne. 
Elk Oosters tapijt is uniek, een creatief kunstwerk elk ontworpen door iemand met zijn eigen verhaal. 
Er zijn zo veel variaties, kleuren en patronen die je in een tapijt kan verwerken 
dat er altijd genoeg tapijten zijn die uw huis, kantoor of winkel kunnen verfraaien. <br>
    <img src='/static/npt/images/carpetinroom.jpg' width='100%' height='100%'></img>
    <figcaption> <i style='font-size: 0.8rem; word-spacing: 1px;'> 
        Een Oosters tapijt in een moderne ruimte
    </i> </figcaption>
"""

f2.a = """<b> Ja natuurlijk. </b> Uw tapijt zal niet worden beschadigd als u het op een verwarmde vloer legt."""

f3.a = """
<b> Helaas hebben wij voorlopig nog geen tapijten die geschikt zijn voor in de tuin of op het terras. </b>
Tapijten voor buiten moeten namelijk weersbestendig zijn. 
Dat houdt in dat ze zijn beschermd tegen schadelijke invloeden uit de natuur zoals regen, 
vuil uit de buitenlucht of verkleuring door zonlicht. 
Een Perzisch tapijt is dat bijvoorbeeld niet, want na een regenbui zal de pool worden verhard door het water."""

f4.a = """
<b> Het antwoord is nee. </b> Wij hebben namelijk ook een aantal machinale tapijten. 
Hierin is natuurlijk niet net zoveel energie in gestopt als bij Handgeknoopte tapijten, waardoor het ook minder prijzig is, 
maar ze kunnen alsnog beschikken over mooie patronen en kleuren waardoor ze zeker goed bij uw interieur kunnen passen. 
Uiteraard melden we het wanneer u een machinaal tapijt ziet.""" 

f5.a = """
U heeft net uw interieur verfraaid met een wollen Oosters tapijt. U wil niet dat uw tapijt er dalijk zo uit gaat zien.
<img src=“beschadigdtapijt.png”>
Hier zijn een aantal tips om motten te bestrijden:
<ul>

<li> Motten houden van donkere afgelegen plekjes. 
Zorg er dus voor dat er regelmatig licht schijnt op uw tapijt. 
Vooral wanneer een deel van uw tapijt zich onder een bank vindt of wanneer u een opgerolde tapijt heeft is dit erg belangrijk.
</li>

<li>
Daarnaast houden motten ook van vuil en viezigheden. 
Zorg er dus voor dat uw tapijt schoon blijft. 
Probeer bijvoorbeeld het eten van kruimelig voedsel te vermijden boven uw tapijt. 
Daarnaast is het belangrijk om uw tapijt regelmatig te stofzuigen.
</li>

<li>
Mottenballen kunnen ook meehelpen met het afweren van motten. 
Dit is een klein balletje aan chemische verbindingen en erg onaangenaam voor motten. 
</li>
</ul>

-“Om tapijt te beschermen tegen motten kun je het boenen met een mengsel van water en azijn in de verhouding 1:1”??? """

f6.a = """
Soms is er aan een Perzisch tapijt wel door 2 man 2 jaar aan gewerkt. 
Dat is dus 1 jaar per man! 
Het zijn unieke kunstproducten met de hand vervaardigd en er wordt enorm veel tijd en aandacht aan besteed 
wat resulteert in een buitengewoon goede en fijne kwaliteit. <br>
In relatie met arbeid en materiaal zijn Perzische tapijten dus eigenlijk helmaal niet zo duur! 
Ze zijn wel kostbaar, omdat het waardeobjecten zijn van uiterste klasse."""


f7.a = """
<div class='clearfix'>
    <div class="col-md-4 float-md-end mb-3 ms-md-3">
        <img src='/static/npt/images/Pazyryktapijt.jpg'></img>
        <figcaption> <i style='font-size: 0.8rem; word-spacing: 1px;'> 
            Een deel van het Pazyryk tapijt; het oudste tapijt tot nu toe gevonden 
        </i> </figcaption>
    </div>
    Het oudste tapijt dat tot nu toe is gevonden is het Pazyryk tapijt daterend uit de 5de eeuw voor Christus. 
    Het is ontdekt in Siberië en het was beschermd door dik laag ijs waardoor het goed bewaard is gebleven.
    De Griekse historicus Herodotus schreef in diezelfde periode over hoe de bewoners van Kaukasus prachtige tapijten
    maken met wonderlijke kleuren en hij had dus geen ongelijk. 
    De kunst van het knopen van een tapijt bestaat dus al 2500 jaar lang, 
    maar waarschijnlijk gaat de geschiedenis van de tapijt nog verder terug in de tijd. <br>
    De gedachte gaat dat de Egyptenaren en Chinezen al tapijten gebruikten niet alleen ter decoratie, 
    maar ook om hunzelf warm te houden in de winter. 
    Het knopen van tapijten bestaat waarschijnlijk dus al meer dan 10000 jaar 
    en <b> wij van NPT zijn trots dat we de handel van deze eeuwenoude traditie in stand mogen houden!</b>
</div>"""

f8.a = """
<b> Jazeker. </b> Vaak wordt gedacht dat tapijten met fijne kwaliteit ook kwetsbaar zijn, 
Maar eigenlijk zijn ze net zo sterk als vloerbedekking van projectkwaliteit 
en dus zullen ze niet worden beschadigd als je er met schoenen overheen loopt. 
Daarnaast zijn ze goed te reinigen wanneer er vuil op komt."""

f9.a = """
<ul>
<li> China </li>
<li> Thailand </li>
<li> Nepal </li>
<li> India </li>
<li> Rusland </li>
<li> Pakistan </li>
<li> Afghanistan </li>
<li> Iran </li>
<li> Turkije </li>
<li> Algerije </li>
<li> Marokko </li>
<!-- <li> Frankrijk </li> -->
</ul>
"""


f10.a = """Perzische tapijten zijn meestal niet hoogpolig. 
Echter zijn er wel andere handgeknoopte hoogpolige tapijten bijvoorbeeld Chinese tapijten. 
Wij beschikken ook over reliëf geschoren Chinese tapijten in onze collectie. 
Dat houdt in dat figuren in de tapijt worden uitgesneden dankzij deze hoge pool. Zie foto"""

