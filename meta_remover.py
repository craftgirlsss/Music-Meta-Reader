from mutagen.id3 import ID3, ID3NoHeaderError
from mutagen.mp3 import MP3
import shutil

def clean_metadata_v2(mp3_file_path):
    try:
        audio = ID3(mp3_file_path)
        # Display all existing tags
        print("Existing tags:")
        for tag in audio.keys():
            print(f"{tag}: {audio[tag]}")
        
        # Clear all tags (full wipe)
        audio.delete()
        audio.save()
        print(f"Metadata cleaned from {mp3_file_path}")

    except ID3NoHeaderError:
        print("No ID3 header found, nothing to clean.")


def remove_copyright_tags(mp3_path):
    try:
        audio = ID3(mp3_path)

        # List of possible copyright-related tags
        copyright_tags = ['TCOP', 'WCOP', 'TPUB']

        for tag in copyright_tags:
            if tag in audio:
                print(f"Removing tag: {tag}")
                del audio[tag]

        audio.save()
        print("Copyright tags removed successfully.")

    except ID3NoHeaderError:
        print("No ID3 tag found in the file.")

# Example usage
music_directory = input("Input Music Directory: ")


copy = "edited.mp3"
shutil.copyfile(music_directory, copy)
clean_metadata_v2(music_directory)
#remove_copyright_tags(music_directory)

