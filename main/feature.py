class Feature:
    def __init__(self, icon, title, description):
        self.icon = icon
        self.title = title
        self.description = description
        self.it = {"icon": self.icon, "title": self.title, "description": self.description}
    
    def __iter__(self):
        return iter(self.it)