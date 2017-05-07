from datetime import date
from artist import Artist


class Album:
    artist = None
    image = None
    name = None
    release_date = None
    tracks = []

    def __init__(self, json_data):
        self.artist = Artist(json_data['artists'][0])
        self.image = json_data['images'][0]['url']
        self.name = json_data['name']
        precision = json_data['release_date_precision']
        if precision == 'year':
            self.release_date = date(int(json_data['release_date']), 1, 1)
        else:
            date_split = json_data['release_date'].split('-')
            if len(date_split) == 2:
                self.release_date = date(int(date_split[0]), int(date_split[1]), 1)
            else:
                self.release_date = date(int(date_split[0]), int(date_split[1]), int(date_split[2]))

    def __str__(self):
        return "%s (%s)" % (self.name, self.artist.name)

    __repr__ = __str__
