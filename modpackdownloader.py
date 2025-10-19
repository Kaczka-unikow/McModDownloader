from json import load
from dotenv import load_dotenv
import requests
import os


load_dotenv()
path = os.getenv('MODPACK_PATH') #example: "C:\Users\Me\Downloads\Better MC [NEOFORGE] BMC5 v31\modrinth.index.json"




with open(path, "r") as f:
	modlist = load(f)

def main(modlist):
	files = modlist["files"]
	for mod in files:
		try:
			url = mod["downloads"][0]
			file_name = os.path.join(os.getcwd(), mod["path"])
			os.makedirs(os.path.dirname(file_name), exist_ok=True)
			response = requests.get(url)
			file = response.content
			with open(file_name, "wb") as new_file:
				new_file.write(file)
			print(f"Successfully downloaded {mod['path'].replace('mods/', '')}!")
		except requests.exceptions.RequestException as e:
			print(f"Error downloading file: {e}")
		except Exception as e:
			print(f"An unexpected error occurred: {e}")

	print("Successfully downloaded all mods!")


if __name__ == "__main__":
	main(modlist)