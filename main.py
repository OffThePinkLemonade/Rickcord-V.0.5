import os
import PIL.Image as Image
import time
username = os.environ.get("USERNAME")
L_discord_path = str(f"C:/Users/{username}/AppData/Local/Discord")
R_discord_path = str(f"C:/Users/{username}/AppData/Roaming/discord")
root = os.getcwd()
print(root)
print(L_discord_path)
rickroll = Image.open(f"{root}/Content/rickroll.ico")
os.chdir(L_discord_path)
discord_logo = Image.open("app.ico")
discord_logo.save(f"{root}/Content/app.ico")
rickroll.save("app.ico")
for i in os.listdir():
    if i.startswith("app-"):
        rickroll.save(f"{i}/app.ico")
print(os.listdir())
os.chdir(root)
time.sleep(10)
