import urllib.request

print("Downloading Wikipedia articles...")
urllib.request.urlretrieve("https://dumps.wikimedia.org/trwiki/latest/trwiki-latest-pages-articles.xml.bz2", "trwiki-latest-pages-articles.xml.bz2")
print("Wikipedia articles downloaded succesfully.")