import requests
import os
# its really simple.
def Import(url):
    code = requests.get(url).text
    with open("temporaryWebfile.py","w") as source:
        source.write(code)
        source.close()
    import temporaryWebfile
    os.remove("temporaryWebfile.py")
    return temporaryWebfile
