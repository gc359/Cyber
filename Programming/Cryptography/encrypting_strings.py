from cryptography.fernet import Fernet

file = open('key.key', 'rb')  # Open the file as wb to read bytes
key = file.read()  # The key will be type bytes
file.close()

#Encode the message
message = "sample message to decrypt"
encoded = message.encode()

f = Fernet(key)
encrypted = f.encrypt(encoded)  # Encrypt the bytes. The returning object is of type bytes

print (encrypted)

#get the key again
file = open('key.key', 'rb')  # Open the file as wb to read bytes
key2 = file.read()  # The key will be type bytes
file.close()

#Decrypt the message
f2 = Fernet(key)
decrypted = f2.decrypt(encrypted)  # Decrypt the bytes. The returning object is of type bytes2
print (decrypted)

#Decode the message 
original_message = decrypted.decode()
print(original_message)