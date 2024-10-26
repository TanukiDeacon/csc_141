# this code will make an album

def make_album(album_title, artist_name, num_songs = None):

    albums = {'Album Title': album_title, 'Artist Name' : artist_name}

    if num_songs:
         albums = {'Album Title': album_title, 'Artist Name' : artist_name, 'Number of Songs' : num_songs}
    return albums


album = make_album('Silver Scream', 'INK')

print (album)

album = make_album('Silver Scream 2: Welcome to HorrorWood', 'INK')

print (album)

album = make_album('Circus of Doom', 'Battle Beast')

print (album)

album = make_album('Unimagine', 'Hands like Houses', '11')

print (album)