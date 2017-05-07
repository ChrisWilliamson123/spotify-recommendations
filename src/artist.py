class Artist:
    name = None
    id = None
    image = None
    genres = []

    def __init__(self, json_data):
        self.name = json_data['name']
        self.id = json_data['id']

    # def set_data(self, json_data):

    def __str__(self):
        return self.name
