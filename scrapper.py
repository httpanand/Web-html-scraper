from urllib.request import urlopen
url = input("Input URL ")

page = urlopen(url)
html_bytes = page.read()

html = html_bytes.decode("utf-8")
print (html)

file = open("output.html","w" , encoding="utf8") 
file.write(html)
file.close()

