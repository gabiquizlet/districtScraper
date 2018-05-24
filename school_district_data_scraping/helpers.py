# helper methods
def maxPage(soup, attribute, tag, classSearch):
	current_num = []
	max_number = soup.find(tag, class_=classSearch)
	for page_option in max_number:
		current_num.append(int(page_option.attrs[attribute].encode("utf-8")))
	return max(current_num)