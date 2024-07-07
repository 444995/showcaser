from abc import abstractmethod

class BaseSite:
    @abstractmethod
    def __init__(self, site_name):
        self.site_name = site_name

    @abstractmethod
    def get_show_ratings(self, show_title):
        raise NotImplementedError("This method should be overridden by subclasses")
