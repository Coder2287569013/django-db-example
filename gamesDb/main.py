import d_setup
from games.models import Game, Genre

game1 = Game.objects.create(
    name="Test Game 1",
    year=2012,
    rating=4.3
)

game2 = Game.objects.create(
    name="Test Game 2",
    year=1998,
    rating=5.0
)

game3 = Game.objects.create(
    name="Test Game 3",
    year=2013,
    rating=4.5
)

game4 = Game.objects.create(
    name="Test Game 4",
    year=2008,
    rating=4.1
)

game1.genre.create(name="FPS")
game2.genre.add(Genre.objects.get(id=1))
game3.genre.create(name="RPG")
game4.genre.create(name="Strategy")