#!/usr/bin/python3.7
#-8- coding: utf-8 -*-

def change_files(filename, crytoFn, block_size=16):

    with open(filename,'r+b') as _file:
        raw_value = _file.read(block_size)
        while raw_value:
            cipher_value = crytoFn(raw_value)
            # Compara o tamanho do bloco cifrado e plano (plain text)

            if len(raw_value) != len(cipher_value):
                raise ValueError('O valor cifrado {} tem um tamanho diferente do valor plano {}'.forma(
                    len(cipher_value), len(raw_value)))


            _file.seek(- len(raw_value),1)
            _file.write(cipher_value)
            raw_value = _file.read(block_size)
