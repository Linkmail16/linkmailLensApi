from linkmailLensApi import lenSearchUrl
ok = input("URL: ")
len = lenSearchUrl(ok)
print(len.statusCode)