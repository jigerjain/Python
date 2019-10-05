import base64
data = open("test", "r").read()
hello = data.split("\n")
#print hello

for test in hello:
        #print test
        try:
                decoded = base64.b64decode(test)
                print decoded
        except:
                continue
