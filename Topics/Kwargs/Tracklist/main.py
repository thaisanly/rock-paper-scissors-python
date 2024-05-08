def tracklist(**kwargs):
    for author, albums in kwargs.items():
        print(author)
        for album, track in albums.items():
            print(f"ALBUM: {album} TRACK: {track}")
