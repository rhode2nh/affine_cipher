# Overview
This program is a python implementation of the affine cipher.

# Usage
There are three commands line arguments available to use for this program. 
```sh
encrypt plaintext-file output-file a b
```
```encrypt``` takes a plaintext file and encrypts it with the given key pair.
- ```plaintext-file``` is a file with the .txt extension.
- ```output-file``` is the file you want to use to store the encrypted text. If the file is not found, it will be created.
- ```a b``` is a unique key pair of numbers used to encrypt the text.
```sh
decrypt encrypted-file output-file a b
```
```decrypt``` takes an encrypted text file and decrypts it with the given key pair.
- ```encrypted-file``` is the file to be decrypted.
- ```output-file``` is the file you want to use to store the encrypted text. If the file is not found, it will be created.
- ```a b``` is a unique key pair of numbers used to decrypt the text. This must be the same pair that was used to encrypt the text.
```sh
decipher encrypted-file output-file dictionary-file
```
```decipher``` takes an encrypted text file and uses a brute force approach to decipher the given encrypted text file. It uses every key pair combination and uses the pair that matches the most valid words. For every key pair, it will check to see if there are valid words.
- ```encrypted-file``` is the file to be deciphered.
- ```output-file``` is the file you want to store the deciphered text. If the file is not found, it will be created.
- ```dictionary-file``` is a dictionary file to be used to decipher the encrypted file.
