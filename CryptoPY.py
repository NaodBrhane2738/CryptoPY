from pyexpat.errors import messages
from hash import hash_file, verify_hash
from encrypt import aes_enc_dec, rsa_enc_dec
from password import pass_strength, hash_password, check_password
from getpass import getpass

print(r"""
 ██████╗ ██████╗ ██╗   ██╗██████╗ ████████╗██████╗ ██████╗ ██╗   ██╗
██╔════╝ ██╔══██╗╚██╗ ██╔╝██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗╚██╗ ██╔╝
██║      ██████╔╝ ╚████╔╝ ██████╔╝   ██║   ██║  ██║██████╔╝ ╚████╔╝ 
██║      ██╔══██╗  ╚██╔╝  ██╔═══╝    ██║   ██║  ██║██╔═══╝   ╚██╔╝  
╚██████╗ ██║  ██║   ██║   ██║        ██║   ╚██████╔╝██║       ██║   
 ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝        ╚═╝    ╚═════╝ ╚═╝       ╚═╝   
""")
print("\nWelcome!!!")

def menu():
    print("\n Select an option: ")
    print("1. Hash file")
    print("2. Verify hash")
    print("3. AES Encrypt/Decrypt")
    print("4. RSA Encrypt/Decrypt")
    print("5. Password manager")
    print("0. Exit")



while True:
    menu()
    choice = input("Enter Your Choice: ")
    if choice == "0":
        print("Thanks for trying our tool.\nExiting...")
        break
    elif choice == "1":
        file_path = input("Enter filepath: ")
        print(f"\nSHA Hash of file is {hash_file(file_path)} ")
    elif choice == "2":
        file_path1 = input("Enter filepath1: ")
        file_path2 = input("Enter filepath2: ")
        print(verify_hash(file_path1, file_path2))
    elif choice == "3":
        message = input("Enter message: ")
        key, encrpted, decrypted = aes_enc_dec(message)
        print("AES key: ", key)
        print("AES encrpted: ", encrpted)
        print("AES decrypted: ", decrypted)
    elif choice == "4":
        message = input("Enter message: ")
        encrpted, decrypted = rsa_enc_dec(message)
        print("RSA encrpted with private key: ", encrpted)
        print("RSA decrypted wit private key: ", decrypted)
    elif choice == "5":
        while True:
            password1 = getpass("Enter password to check strength: ")
            print(pass_strength(password1))
            if pass_strength(password1).startswith("Weak"):
                print(f"{password1} is a Weak password, please try stronger password.")
            else:
                print(f"{password1} is a strong password.")
                break
        hashed_password = hash_password(password1)
        print("The Hashed Password is", hashed_password)
        attempt = getpass("re-enter teh password to verify: ")
        print(check_password(attempt, hashed_password))
    else:
        print("Invalid choice. Please try again.")

print("Thanks for trying our tool.")