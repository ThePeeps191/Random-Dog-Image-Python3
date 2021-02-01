import requests, json

s = json.loads(requests.get("https://dog.ceo/api/breeds/image/random").text)

with open("img.txt", 'w') as f:
	f.write(s['message'])

# Go To img.txt To See The Image Link
