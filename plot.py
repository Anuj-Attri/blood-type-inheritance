# Visualise our output

def bar_plot(data_dict, title=""):
	"""
	This function can plot a vertical bar graph, given a dictionary.
	
	Optional: Title to the bar graph can be set by "title=". Default None.
	"""
	keys = list(data_dict.keys())
	values = list(data_dict.values())
	print("---------------------------")
	print(title)
	for i in range(len(keys)):
		print(keys[i] + ": " + "■"*(round(values[i])))