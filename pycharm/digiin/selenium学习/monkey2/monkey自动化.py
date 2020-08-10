import subprocess
a = subprocess.getoutput("adb devices")
print(a)
b = a.replace("no permissions","").replace("device","").replace("\t","").split("\n")[1:-1]
print("-------")
print(b)