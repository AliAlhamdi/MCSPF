from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa

''' The function will decrypt the msg, using the the private
key from load_key() func'''


def decrypt(encrypted_data):
    pk = load_pr_key()
    pk.decrypt(encrypted_data, padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA1()),
        algorithm=hashes.SHA1(),
        label=None
        )
    )


'''this func shall load the private key from the .pem file.'''


def load_pr_key():
    with open('pr_key.pem', 'rb') as file:
        pem_lines = file.read()

    private_key = serialization.load_pem_private_key(pem_lines,
                                                     None, default_backend())
    return private_key


'''this func shall load the public key from the .pem file.'''


def load_pu_key():
    with open('pu_key.pem', 'rb') as file:
        pem_lines = file.read()
    public_key = serialization.load_pem_public_key(pem_lines,
                                                   default_backend())
    key = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1,
    )
    return key


''' This func will create a Private and it's
    Public key and store it in a .pem files.'''


def create_keys():
    private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
            )
    public_key = private_key.public_key()

    # convert the private key into bytes to be written as .pem file.
    pr_pem = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption()
        )
    pu_pem = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1,
    )

    with open('pr_key.pem', 'wb') as private_file:
        private_file.write(pr_pem)
    with open('pu_key.pem', 'wb') as public_file:
        public_file.write(pu_pem)

create_keys()
