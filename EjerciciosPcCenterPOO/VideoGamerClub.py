class VideoGamerClub:
    total_members = 0
    games_collection = []

    def __init__(self):
        self.members = []

    @classmethod
    def add_member(cls, member_name):
        cls.total_members += 1
        instance = cls()
        instance.members.append(member_name)
        return instance

    @classmethod
    def add_game(cls, game_name):
        cls.games_collection.append(game_name)

    @classmethod
    def get_total_members(cls):
        return cls.total_members

    @classmethod
    def get_games_collection(cls):
        return cls.games_collection


club = VideoGamerClub()


club_instance_1 = VideoGamerClub.add_member("Juan")
club_instance_2 = VideoGamerClub.add_member("Maria")


VideoGamerClub.add_game("The Legend of Zelda")
VideoGamerClub.add_game("Super Mario Bros")


total_members = VideoGamerClub.get_total_members()
print(f"Total de miembros: {total_members}")


games_collection = VideoGamerClub.get_games_collection()
print("Colección de juegos:", games_collection)