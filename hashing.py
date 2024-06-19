import hashlib
import os
import sys
import platform

clear = "gravita sigmaa"
os_name = platform.system()
if os_name == "Linux":
    clear = "clear"
else:
    clear = "cls"

target = input("Input the string you want to hash / შეიყვანე სტრინგი რომელიც გინდა რომ დაჰაშო: ")
os.system(clear)


print("[1] md5")
print("[2] sha1")
print("[3] sha256")
algorithm = input("Choose your algorithm / აირჩიე დაჰაშვის ალგორითმი: ")


def hashing(target, algorithm):
    if algorithm == "1":
        hashed_object = hashlib.md5(target.encode())
        os.system(clear)
    elif algorithm == "2":
        hashed_object = hashlib.sha1(target.encode())
        os.system(clear)
    elif algorithm == "3":
        hashed_object = hashlib.sha256(target.encode())
        os.system(clear)
    else:
        os.system(clear)
        return "Unsupported algorithm or invalid choice / არამხარდაჭერილი ალგორითმი ან არასწორი არჩევანი"
        sys.exit()
    os.system(clear)
    return hashed_object.hexdigest()
    

print(f"Hashed string: {hashing(target, algorithm)} / დაჰაშული სტრინგი: {hashing(target, algorithm)}")