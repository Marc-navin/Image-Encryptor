from cryptography.fernet import Fernet
import os

key=Fernet.generate_key()

if not os.path.exists("key1.key"):
    with open("key1.key", "wb") as f:
        f.write(Fernet.generate_key())

with open("key1.key", "rb") as f:
    key = f.read()

cipher = Fernet(key)

def encryptor(image):
    with open(image, 'rb') as f:
        original=f.read()
    encrypted=cipher.encrypt(original)

    with open(f'{image}.encrypted','wb') as f:
        f.write(encrypted)
    print(f'{image}_encrypted.jpg is the encrypted image file')

def decryptor(image):
    with open(image,'rb') as f:
        encrypted_data=f.read()

    decrypted=cipher.decrypt(encrypted_data)

    with open(f'{image}_decrypted.jpg' , 'wb') as f:
        f.write(decrypted)
    print(f'{image}_decrypted.jpg is the decrypted image file')

image_link=input(" Enter the image path (e.g. 'cat.jpg' or 'img.jpg.encrypted'):")
ch=0
if os.path.exists(image_link):
    while ch!=3:
        print('1. Encrypt the image\n 2.Decrypt the image \n 3.Exit')
        ch=int(input('Enter your choice:'))
        if ch==1:
            encryptor(image_link)
        elif ch==2:
            decryptor(image_link)
        elif ch==3:
            break
        else:
            print('Invalid choice')

else:
    print('The image is not found')
        
    
