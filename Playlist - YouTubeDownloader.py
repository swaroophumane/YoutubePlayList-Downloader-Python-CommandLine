import pytube
from pytube import Playlist
import os

while True:
	while True:
		foldername = input("Please Enter Folder Name (Where all the videos will saved): - ").strip()
		if len(foldername) > 0:
			break

	if not os.path.exists(f'D:/Download-YouTube Videos/{foldername}'):
		os.makedirs(f'D:/Download-YouTube Videos/{foldername}')
		os.chdir(f'D:/Download-YouTube Videos/{foldername}')
	else:
		os.chdir(f'D:/Download-YouTube Videos/{foldername}')

	try:
		playlist_url = input("Please Enter Youtube Playlist Link : ")
		myplaylist = Playlist(playlist_url)
		print()
		print("Downloading Stared.. Please Wait, This may take time (Depends on Number of Videos)")
		myplaylist.download_all(f'D:/Download-YouTube Videos/{foldername}')
		print("Downloading Finished..")
		print()
	except:
		print("Please Check Your URL, Is it a Playlist URL?")
		print()

	MoreVideo = input("Do You Wants to Download More Video? (Yes/No) :- ").lower()
	print()
	if MoreVideo == 'yes':
		continue
	else:
		break
	print()

print(f"Video Saved in - D:/Download-YouTube Videos/")
print()
