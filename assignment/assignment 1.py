Track_code=input("enter track code (int):")
Playlist_name=input("enter playlist name(str):" )
Total_playtime=float(input("enter total playtime:"))
Song_categories=input("enter song categories (comma-seperated):").split(',')
Tracks_in_playlist=tuple(map(int,input("enter tracks in playlist(tuple): ").strip('()')))
Tracks_played=tuple(map(int,input("enter tracks played(tuple):").strip('()')))
Premium_offer=float(input("enter premium offer (%): "))
Audio_enhancements=set(input("enter audio enhancements)(set): ").split(','))
Music_curator=input("enter music curator: ")
Contact_handle=input("enter contact handle: ")
Playlist_region=input("enter playlist region: ")
Curator_info= {
    "Music_curator":Music_curator,
    "Contact_handle":Contact_handle,
    "Playlist_region":Playlist_region
}
# using comma seperation(sep',')
print("\ntrack code,playlist name,total playlists:",Track_code,Playlist_name,Total_playtime, sep=',')
# using percentage formatting (% operator)
print("premium offer:%.2f%%" % Premium_offer)
#using f-strings(f"")
print(f"Track code:{Track_code}")
print(f"playlist name:{Playlist_name}")
print(f"Total playtime:{Total_playtime}")
print(f"Song catogories:{Song_categories}")
print(f"Tracks in playlist:{Tracks_in_playlist}")
print(f"Tracks played:{Tracks_played}")
print(f"Premium offfer:{Premium_offer}")
print(f"Audio enhancements:{Audio_enhancements}")
print(f"Music curator:{Music_curator}")
print(f"Contact handle:{Contact_handle}")
print(f"Playlist region:{Playlist_region}")
#using .format() method
print("Curator:Music-{},Cotact-{},Region{}".format(Curator_info["Music_curator"],Curator_info["Contact_handle"],Curator_info["Playlist_region"]))