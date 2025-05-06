class MusicMetaReader:
    def withTinyTag(self, urlSong: str):
        from tinytag import TinyTag
        try:
            tag = TinyTag.get(urlSong)
            print(f'Artist: {tag.artist}')
            print(f'Title: {tag.title}')
            print(f'Album: {tag.album}')
            print(f'Track: {tag.track}')
            print(f'Duration: {tag.duration:.2f} seconds')
            print("\n")
        except FileNotFoundError:
            print("Error: The specified file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def withMutagen(self, urlSong: str):
        from mutagen.mp3 import MP3
        try:
            audio = MP3(urlSong)
            print(f'Artist: {audio.get("TPE1")[0]}')
            print(f'Title: {audio.get("TIT2")[0]}')
            print(f'Album: {audio.get("TALB")[0]}')
            print(f'Track: {audio.get("TRCK")[0]}')
            print(f'Duration: {audio.info.length:.2f} seconds')
            print("\n")
        except FileNotFoundError:
            print("Error: The specified file was not found.")
        except Exception as e:
            print(f"An error occurred: {e}")

    def runner(self):
        urlDirectory: str = input("Inputkan Mokasi Musik (format mp3): ")
        self.withTinyTag(urlSong = urlDirectory) 
        self.withMutagen(urlSong = urlDirectory)


reader: MusicMetaReader = MusicMetaReader()
reader.runner()