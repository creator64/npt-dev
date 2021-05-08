from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Carpet
from .filter_carpets import filter_carpets


DEFAULT_FORM_INFO = {"prf_width": "", "prf_height": "",
					 "prf_accuracy": 10,
					 "prf_style": "Alle",
					 "prf_material": "Alle",}

# this is a comment


def check_prf(arg, prf):
	if bool(arg):
		return arg
	return DEFAULT_FORM_INFO[prf]


def create_prf(info):
	output = {}
	output["prf_width"] = check_prf(info.get("prf_width"), "prf_width")
	output["prf_height"] = check_prf(info.get("prf_height"), "prf_height")
	output["prf_accuracy"] = check_prf(info.get("prf_accuracy"), "prf_accuracy")
	output["prf_style"] = check_prf(info.get("prf_style"), "prf_style")
	output["prf_material"] = check_prf(info.get("prf_material"), "prf_material")

	return output


# Create your views here.

def collection(response):
	carpets = Carpet.objects.all()
	info = response.GET
	prf = create_prf(info)

	valid_carpets = list(filter(lambda carpet: filter_carpets(carpet, prf), carpets)) 
	paginator = Paginator(valid_carpets, 4)

	page_number = info.get('page')
	page_obj = paginator.get_page(page_number)
	pages = page_obj.paginator.num_pages

	return render(response, "collection/collection.html", {"actdict": {"collec": "active",},
														   "carpets": page_obj,
														   "prf": prf,
														   "range_pages": range(1, pages+1)
														   })

def view(response, id):
	id = id - 102345
	carpet  = Carpet.objects.get(id=id)
	return render(response, "collection/view.html", {"actdict": {"collec": "active",},
													 "carpet": carpet})
