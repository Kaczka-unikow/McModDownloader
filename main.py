from json import load
from time import sleep
import requests
import os




def main():
	path = os.path.join(os.getcwd(),"mods.json")
	download_dir = os.path.join(os.getcwd(), "downloads")
	os.makedirs(os.path.dirname(download_dir), exist_ok=True)
	try:
		with open(path, "r") as file:
			modlist = load(file)
	except Exception as e:
		print("Some error occurred: ")
		print(e)
		print(f"Prodobly {path} doesn't exist or have bad construction")
		input()
		return
	print("Hello!")
	print("Welcome to simple mod downloader!")
	print("This project is licensed under Creative Commons Attribution-NonComercial-ShareAlike 4.0 International License")



	for mod_key in modlist.keys():
		try:
			url = modlist[mod_key]
			file_name = os.path.join(download_dir, f'{mod_key}.jar')
			response = requests.get(url)
			file = response.content
			os.makedirs(os.path.dirname(file_name), exist_ok=True)
			with open(file_name, "wb") as new_file:
				new_file.write(file)
			print(f"Successfully downloaded {mod_key}.jar!")
		except requests.exceptions.RequestException as e:
			print(f"Error downloading file: {e}")
		except Exception as e:
			print(f"An unexpected error occurred: {e}")
	
	print("Downloading finished")
	input()
	

if __name__ == "__main__":
	main()