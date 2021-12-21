import time

# Mudar aqui os valores
source_file = 'zebra.bmp'
destination_file = 'RLE'
extension = '.dat'


def main():
    start_timer = time.time()
    data = read_file(source_file)
    data_array = bytearray(data)
    run = rle_encode(data_array)
    write_file(destination_file + extension, run)
    print("Tempo de execução: " + str(round((time.time() - start_timer), 2)) + "s")




def rle_encode(data):
    encoding = bytearray()
    previous_value = ''
    contador = 1

    for value in data:

        if value != previous_value:
            if previous_value:
                if contador > 2:
                    if contador >= 256:
                        encoding += contador.to_bytes(3, byteorder='little')
                    else:
                        encoding.append(contador)
                    encoding.append(previous_value)
                else:
                    for i in range(contador):
                        encoding.append(previous_value)
            contador = 1
            previous_value = value
        else:
            contador += 1
    return encoding


# Escrever bytearray para ficheiro
def write_file(filename, data):
    with open(filename, 'wb') as f:
        f.write(data)
        f.close()


# le bytearray do ficheiro
def read_file(filename):
    with open(filename, 'rb') as f:
        data = f.read()
        f.close()
        return data





if __name__ == "__main__":
    main()
