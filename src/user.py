from album import Album


class User:
    id = None
    name = None
    premium = False
    date_of_birth = None
    country = None
    albums = []
    artists = []

    def __init__(self, user_data):
        self.id = user_data['id']
        self.name = user_data['display_name']
        self.premium = True if user_data['product'] == 'premium' else False
        self.date_of_birth = user_data['birthdate']
        self.country = user_data['country']

    def set_albums(self, albums_json):
        for a in albums_json:
            self.albums.append(Album(a))



    def __str__(self):
        return self.id


