class Episode:
    def __init__(self, title, episode_number, season_number, rating):
        self.title = title
        self.episode_number = episode_number
        self.season_number = season_number
        self.rating = rating

    def get_title(self):
        return self.title

    def get_episode_number(self):
        return self.episode_number

    def get_season_number(self):
        return self.season_number

    def get_rating(self):
        return self.rating
