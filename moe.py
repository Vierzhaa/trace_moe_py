import requests, os
import urllib.parse

def c():
    os.system("cls" if os.name == "nt" else "clear")

def back(m=None):
    if m:
        print(m)
    input("Press Enter to continue...")
    c()

def search(op,query):
    if op == "file":
        if not os.path.isfile(query):
            print("File does not exist.")
            return None
        response = requests.post(
            "https://api.trace.moe/search?anilistInfo",
            data=open(query, "rb"),
            headers={"Content-Type": "image/jpeg"}
        )
    elif op == "url":
        response = requests.get(
            f"https://api.trace.moe/search?anilistInfo&url={urllib.parse.quote_plus(query)}"
        )
    else:
        print("Invalid search option.")
        return None

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}")
        return None

c()
while True:
    options = input("Choose an option:\n1. Search by image file\n2. Search by image URL\n3. Exit\n> ")
    if options == "1":
        file_path = input("Enter the path to the image file: ")
        if not os.path.isfile(file_path):
            print("File does not exist.")
        else:
            n=search("file", file_path)
            if n:
                for s,i in enumerate(n['result'],1):
                    print(f"Result {s}\nenglish title: {i['anilist']['title']['english']}\nromaji title: {i['anilist']['title']['romaji']}\nEpisode: {i['episode']}\nSimilarity: {i['similarity']:.2%}\nFrom: {i['from']:.2f}s to {i['to']:.2f}s\nVideo: {i['video']}\nanilist id: {i['anilist']['id']}\n")
            if input("Do you want to search again? (y/n): ").lower() != "y":
                break
            c()
    elif options == "2":
        image_url = input("Enter the image URL: ")
        #sample: "https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg"
        n=search("url",image_url)
        if n:
            for s,i in enumerate(n['result'],1):
                print(f"Result {s}\nenglish title: {i['anilist']['title']['english']}\nromaji title: {i['anilist']['title']['romaji']}\nEpisode: {i['episode']}\nSimilarity: {i['similarity']:.2%}\nFrom: {i['from']:.2f}s to {i['to']:.2f}s\nVideo: {i['video']}\nanilist id: {i['anilist']['id']}\n")
        if input("Do you want to search again? (y/n): ").lower() != "y":
                break
        c()
    elif options == "3":
        c()
        print("bye")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")
        back()
        continue




