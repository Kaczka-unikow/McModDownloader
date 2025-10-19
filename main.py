from json import load
import requests
import os

path = os.path.join(os.getcwd(),"mods.json")
download_dir = os.getcwd()
with open(path, "r") as file:
	modlist = load(file)
print(modlist)



for mod_key in modlist.keys():
	try:
		url = modlist[mod_key]
		file_name = os.path.join(os.getcwd(), f'{mod_key}.jar')
		response = requests.get(url)
		file = response.content
		with open(file_name, "wb") as new_file:
			new_file.write(file)
		print(f"Udało się pobrać {mod_key}.jar!")
	except requests.exceptions.RequestException as e:
		print(f"Błąd podczas pobierania pliku: {e}")
	except Exception as e:
		print(f"Wystąpił nieoczekiwany błąd: {e}")
	
