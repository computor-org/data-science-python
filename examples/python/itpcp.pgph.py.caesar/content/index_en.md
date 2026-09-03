<!-- Caesar source wiki -->
[caesar]: <https://en.wikipedia.org/wiki/Caesar_cipher> "caesar"

# Caesar Cipher

## Introduction

The [Caesar cipher][caesar] is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet.

The encryption works through a cyclic shift of the letters. The shift is determined by a parameter known as the key:

For example, the word "Hello" encrypted with a key of $z=3$ becomes "Khoor".
Here $z$ indicates the number of positions each letter is shifted in the alphabet.

For the key $z=3$, the encryption table looks as follows:

| Plaintext | A | B | C | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z |
|-----------|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Ciphertext | D | E | F | G | H | I | J | K | L | M | N | O | P | Q | R | S | T | U | V | W | X | Y | Z | A | B | C |


## Task

### 1. Encryption & Decryption

1. Write a function `caesar_encrypt(text: str, key: int, alphasize: int = 85) -> str` that encrypts a text `text` with a key `key`. The alphabet has a size of `alphasize` characters.

2. Write a function `caesar_decrypt(text: str, key: int, alphasize: int = 85) -> str` that decrypts an encrypted text `text` with a key `key`. The alphabet has a size of `alphasize` characters.

3. Both functions should work for all keys $0 \leq z$ (if $z$ is greater than the number of letters in the alphabet, the shift should wrap around; i.e., $z=\mathrm{alphasize} + 1$ encrypts the same as $z=1$).

### 2. Code Breaking

Now let's crack some codes!

1. Read the text from the file `enc.txt` and decrypt it. Note the following:

    The text is divided into 3 subsections, each encrypted differently and progressively harder to decrypt.

    1) Well this is easy: This text was encrypted with an unknown key, try to crack it. Save the decrypted text in the file `dec1.txt`.
    2) This is a bit harder: Perhaps the lines in this text are encrypted differently. The title and text from 1) might give a hint. Are there character sequences that occur frequently? Save the decrypted text in the file `dec2.txt`.
    3) This is the hardest: This is probably even more difficult. Perhaps there are tips in text 2). Save the decrypted text in the file `dec3.txt`.

#### Have fun cracking!
