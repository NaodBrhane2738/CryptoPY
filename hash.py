import hashlib



# text = input("Enter the text: ")
#
# hash_txt = hashlib.sha256(text.encode()).hexdigest()
#
# print(f'{text} is hashed to {hash_txt}')

# file_path = input("Enter the file path: ")


def hash_file(file_path):
    h = hashlib.new("sha256")
    with open(file_path, "rb") as file:
        while True:
            content = file.read(1024)
            if content == b"":
                break
            h.update(content)
    return h.hexdigest()

def verify_hash(file1, file2):
    hash1 = hash_file(file1)
    hash2 = hash_file(file2)
    print(f"\nChecking Changes and modifications between {file1} and {file2}")
    if hash1 == hash2:
        return "Files are secure, no changes or modifications have been made. "
    else:
        return "\nLook out. Files has been modified, Possibly not secured"

if __name__ == "__main__":
    file1 = input("Enter filepath 1: ")
    file2 = input("Enter filepath 2: ")
    # print(f'{file_path} is hashed to {hash_file(file_path)}')
    print(verify_hash(file1, file2))



