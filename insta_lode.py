import instaloader

data = instaloader.Instaloader()

username = input("enter profile name : ")

data.download_profile(username,profile_pic_only=True)