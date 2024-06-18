a = input("File name: ").lower().replace(" ", "")

if ".gif" in a:
    print("image/gif")
elif ".jpg" in a:
    print("image/jpeg")
elif ".jpeg" in a:
    print("image/jpeg")
elif ".png" in a:
    print("image/png")
elif ".pdf" in a:
    print("application/pdf")
elif ".txt" in a:
    print("text/plain")
elif ".zip" in a:
    print("application/zip")
else:
    print("application/octet-stream")
