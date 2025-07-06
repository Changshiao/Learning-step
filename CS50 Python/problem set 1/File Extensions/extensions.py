msg=input("type of file? ").lower()
if '.jpg' in msg:
    print("image/jpeg")

elif '.pdf' in msg:
    print("application/pdf")

elif '.png' in msg:
   print("image/png")

elif '.zip' in msg:
    print("application/zip")

elif '.gif' in  msg:
    print("image/gif")

elif '.txt' in msg:
    print("text/plain")

elif '.jpeg' in msg:
    print("image/jpeg")

else:
    print("application/octet-stream")
