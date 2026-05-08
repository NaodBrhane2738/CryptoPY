import secrets
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes

#symetric encryption
def aes_enc_dec(message):
    key = secrets.token_bytes(32)
    token = secrets.token_bytes(12)
    aes = AESGCM(key)

    encrypted = token + aes.encrypt(token, message.encode(), None)
    decrypted = aes.decrypt(encrypted[:12], encrypted[12:], None)
    return key.hex(), encrypted.hex(), decrypted.decode()


#asymetric encryption
def rsa_enc_dec(message):
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    encrypted = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf = padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    decrypted = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    return encrypted.hex(), decrypted.decode()



if __name__ == "__main__":
    print(aes_enc_dec("Check"))
    print(rsa_enc_dec("Double Check"))