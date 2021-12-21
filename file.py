import bz2
import lzma
import deflate
import time

# Mudar aqui os valores
source_file = 'egg.bmp'
extension = '.dat'

destination_file = source_file.split('.')[0]  # Separar a extensão do ficheiro

def main():

    print('[1] - Compression')
    print('[2] - Decompression')
    x = int(input('Choose method: '))

    print('[1] - BZIP2')
    print('[2] - LZMA')
    print('[3] - DEFLATE')
    y = int(input('Choose algorithm: '))

    if x == 1:
        if y == 1:
            start_timer = time.time()
            bzip2_method()
            print("Tempo de execução: " + str(round((time.time() - start_timer), 2)) + "s")
        if y == 2:
            start_timer = time.time()
            lzma_method()
            print("Tempo de execução: " + str(round((time.time() - start_timer), 2)) + "s")
        if y == 3:
            start_timer = time.time()
            deflate_method()
            print("Tempo de execução: " + str(round((time.time() - start_timer), 2)) + "s")

    elif x == 2:
        if y == 1:  # BZIP2
            start_timer = time.time()
            decompress(1)
            print("Tempo de execução: " + str(round((time.time() - start_timer), 2)) + "s")
        if y == 2:  # LZMA
            start_timer = time.time()
            decompress(3)
            print("Tempo de execução: " + str(round((time.time() - start_timer), 2)) + "s")
        if y == 3:  # DEFLATE
            start_timer = time.time()
            decompress(2)
            print("Tempo de execução: " + str(round((time.time() - start_timer), 2)) + "s")




def bzip2_method():
    #  BZIP2 Method
    with open(source_file, 'rb') as data:
        contents = bz2.compress(data.read(), 9)  # Default
    f = open(destination_file + '_bzip2' + extension, "wb")
    f.write(contents)
    f.close()


def lzma_method():
    #  LZMA Method
    data = open(source_file, "rb").read()
    contents = lzma.LZMAFile(destination_file + '_lzma' + extension, mode="wb")
    contents.write(data)
    contents.close()


def deflate_method():
    #  DEFLATE Method
    with open(source_file, 'rb') as data:
        contents = deflate.gzip_compress(data.read(), 6)  # Default
    f = open(destination_file + '_deflate' + extension, "wb")
    f.write(contents)
    f.close()


def decompress(opc):
    if opc == 1:  # BZIP2
        with open(destination_file + '_bzip2' + extension, 'rb') as data:
            contents = bz2.decompress(data.read())
        f = open('decompress.bmp', "wb")
        f.write(contents)
        f.close()
    if opc == 2:  # DEFLATE
        with open(destination_file + '_deflate' + extension, 'rb') as data:
            contents = deflate.gzip_decompress(data.read())
        f = open('decompress.bmp', "wb")
        f.write(contents)
        f.close()
    if opc == 3:  # LZMA
        contents = lzma.LZMAFile(destination_file + '_lzma' + extension, mode="rb")
        data = contents.read()
        f = open('decompress.bmp', "wb")
        f.write(data)
        f.close()





if __name__ == "__main__":
    main()
