from cryptography.fernet import Fernet, InvalidToken
key = b'' # Use one of the methods to get a key (it must be the same as used in encrypting)
input_file = 'test.encrypted'
output_file = 'test.txt'

with open(input_file, 'rb') as f:
    data = f.read()  # Read the bytes of the encrypted file

fernet = Fernet(key)
try:
    decrypted = fernet.decrypt(data)

    with open(output_file, 'wb') as f:
        f.write(decrypted)  # Write the decrypted bytes to the output file

    # Note: You can delete input_file here if you want
except InvalidToken as e:
    print("Invalid Key - Unsuccessfully decrypted")