import requests

#the required first parameter of the 'get' method is the 'url':
x = requests.get('https://probityhublabs.com/home/index.html/about/index.html')

#print the response text (the content of the requested file):
# print(x.text)


with open("about_us.html", "w", encoding="utf-8") as file:
    file.write(x.text)

print("Response saved to about_us.html")