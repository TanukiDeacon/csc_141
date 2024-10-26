def make_album(album_title, artist_name, num_songs = None):

    albums = {'Album Title': album_title, 'Artist Name' : artist_name}

    if num_songs:
         albums = {'Album Title': album_title, 'Artist Name' : artist_name, 'Number of Songs' : num_songs}
    return albums


while True:
    print ('\nEnter an album name: ')
    print("(enter 'q' at any time to quit)")

    nameAlbum = input("Album Title: ") 
    if nameAlbum == 'q':
        break 

    artistName = input("Artist name: ") 
    if artistName == 'q':
        break 

    userAlbum = make_album(nameAlbum, artistName)
    print(userAlbum)
