import subprocess

print("Fetching wifi passwords saved on this device...")

data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8').split('\n')
profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]

f = open('spyder_saved.txt', 'a')
f.write("\nThese are some new passwords...\n\n")
f.close

for i in profiles:
    results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8').split('\n')
    results = [b.split(":")[1][1:-1] for b in results if "Key Content" in b]
    try:
        heh = "{:<30}|  {:<}".format(i, results[0])

        f = open('spyder_saved.txt', 'a')
        f.write(f"{heh}\n")
        f.close()
    
    except IndexError:
        f = open('spyder_saved.txt', 'a')
        f.write("Open file in admin mode... \n")
        f.close()

print("Work done sir\nSpyder signing off...")