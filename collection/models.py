from django.db import models
from django.utils.html import format_html


# Create your models here.


class Carpet(models.Model):
	#choices
	CHOICES_MATERIAL = [("Wol", "wol"), ("Zijde", "zijde"), ("Kunststof", "kunststof"),]

	#Fields
	image = models.ImageField()
	price = models.FloatField()
	origin = models.CharField(max_length=50)
	style = models.CharField(max_length=50)
	material = models.CharField(max_length=50, choices=CHOICES_MATERIAL)
	width = models.IntegerField()
	height = models.IntegerField()
	fineness = models.IntegerField()
	description = models.TextField(default="")
	sold = models.BooleanField()

	def image_tag(self):
		if self.image:
			return format_html('<img src="%s" style="width: 120px; height:200px;" />' % self.image.url)
		else:
			return "No Image Found"

	image_tag.short_description = 'Image'
	image_tag.allow_tags = True