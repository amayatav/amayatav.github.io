from dj_equipment import Artist,Album,Track
from hubs import BaseSonicHub
from player import menu

#TODO implement FileBasedSonicHub 

class FileBasedSonicHub(BaseSonicHub):
    '''Reads music files and stores them in a sonic hub!'''
    def __init__(self,name):
        '''Creates an instance of a file-based sonic hub'''
        BaseSonicHub.__init__(self,name)
    
    def populate_maps(self):
        '''Populates the sonic hub with different music and artists'''
        with open("encoded/artists.txt","r") as f:
            for line in f:
                newartist = Artist.deserialize(line.strip())
                self._artist_map[newartist.get_id()] = newartist

        with open("encoded/albums.txt","r") as f:
            for line in f:
                newalbum = Album.deserialize(line.strip())
                self._album_map[newalbum.get_id()] = newalbum

        with open("encoded/tracks.txt","r") as f:
            for line in f:
                newtrack = Track.deserialize(line.strip())
                self._track_map[newtrack.get_id()] = newtrack
                   

if __name__ == "__main__":

    try:
        sonic_hub = FileBasedSonicHub("File Based Sonic Hub")
        print(sonic_hub)
        sonic_hub.populate_maps()
        print(sonic_hub)
        sonic_hub.cross_pollinate()

        menu(sonic_hub)

    except Exception as e:
        print("Could not run our program due to error",e)
