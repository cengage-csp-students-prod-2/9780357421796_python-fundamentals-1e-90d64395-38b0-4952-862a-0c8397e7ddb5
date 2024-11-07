# Write your code here
class WebBrowser:
	def __init__(self, page):
		self.history = [page]
		self.current_page = page
		self.is_incognito = False