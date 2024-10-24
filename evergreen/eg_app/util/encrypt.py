import bcrypt




def encrypt(plaintext):

    # encode plaintext string to bytes
    plaintext = plaintext.encode('')

    bcrypted_plaintext = bcrypt.hashpw(plaintext, bcrypt.gensalt())

    return bcrypted_plaintext