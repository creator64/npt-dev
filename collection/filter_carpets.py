def filter_carpets(carpet, prf):
	if not carpet.sold:
		if carpet.style == prf["prf_style"] or prf["prf_style"] == "Alle":
			if carpet.material == prf["prf_material"] or prf["prf_material"] == "Alle":
				if size_ok(carpet, prf):
					return True
	return False


def size_ok(carpet, prf):
	try:
		req_width = int(prf["prf_width"])
		req_height = int(prf["prf_height"])
	except:
		return True

	req_acc = int(prf["prf_accuracy"])

	#first check normally
	if carpet.width >= (req_width -  req_acc) and carpet.width <= (req_width + req_acc):
		if carpet.height >= (req_height -  req_acc) and carpet.height <= (req_height + req_acc):
			return True

	#second check reversed (so width is height and height is width)
	if carpet.width >= (req_height -  req_acc) and carpet.width <= (req_height + req_acc):
		if carpet.height >= (req_width -  req_acc) and carpet.height <= (req_width + req_acc):
			return True
	return False
