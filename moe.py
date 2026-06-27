import requests, os
import urllib.parse

def c():
    os.system("cls" if os.name == "nt" else "clear")

def back(m=None):
    if m:
        print(m)
    input("Press Enter to continue...")
    c()
def goto(x, y):
    print(f"\033[{x};{y}H", end="")


c()
while True:
    options = input("Choose an option:\n1. Search by image file\n2. Search by image URL\n3. Exit\n> ")
    if options == "1":
        file_path = input("Enter the path to the image file: ")
        if not os.path.isfile(file_path):
            print("File does not exist.")
        else:
            n=requests.post("https://api.trace.moe/search?anilistInfo",
            data=open(file_path, "rb"),
            headers={"Content-Type": "image/jpeg"}
            ).json()
            c()
            for s,i in enumerate(n['result']):
                print(f"Result {s+1}\nenglish title: {i['anilist']['title']['english']}\nromaji title: {i['anilist']['title']['romaji']}\nEpisode: {i['episode']}\nSimilarity: {i['similarity']:.2%}\nFrom: {i['from']:.2f}s to {i['to']:.2f}s\nVideo: {i['video']}\nanilist id: {i['anilist']['id']}\n")
            if input("Do you want to search again? (y/n): ").lower() != "y":
                break
            c()
    elif options == "2":
        image_url = input("Enter the image URL: ")
        #sample: "https://images.plurk.com/32B15UXxymfSMwKGTObY5e.jpg"
        n=requests.get("https://api.trace.moe/search?anilistInfo&url={}"
        .format(urllib.parse.quote_plus(image_url))
        ).json()
        c()
        for s,i in enumerate(n['result']):
            print(f"Result {s+1}\nenglish title: {i['anilist']['title']['english']}\nromaji title: {i['anilist']['title']['romaji']}\nEpisode: {i['episode']}\nSimilarity: {i['similarity']:.2%}\nFrom: {i['from']:.2f}s to {i['to']:.2f}s\nVideo: {i['video']}\nanilist id: {i['anilist']['id']}\n")
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




