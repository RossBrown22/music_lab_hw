import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_repository.update()
album_repository.update()

artist_1 = Artist("Queen")
artist_repository.save(artist_1)
artist_2 = Artist("Elton John")
artist_repository.save(artist_2)

artist_repository.select_all()

album = Album("A Night at the Opera", "Pop/Rock", artist_1)
album_repository.save(album)

pdb.set_trace()