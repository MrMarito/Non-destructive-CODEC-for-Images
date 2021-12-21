from rle import read_file, rle_encode
from sais import makeSuffixArray
import time

# Mudar aqui os valores
source_file = 'zebra.bmp'
destination_file = 'transformada'
extension = '.dat'


def ComputeWrapSA(data):
    data2 = data*2
    idxs = makeSuffixArray(data2)
    idxs = [x for x in idxs if x < len(data)]
    return idxs


def EncodeBWT(data):
    idxs = ComputeWrapSA(data)
    bwt, ptr = bytearray(len(data)), 0
    for j, i in enumerate(idxs):
        if i == 0:
            ptr = j
            i = len(data)
        bwt[j] = data[i-1]
    return bwt, ptr


def DecodeBWT(bwt, ptr):
    cumm, n, = [0]*256, 0
    for v, in bwt:
        cumm[v] += 1
    for i, v in enumerate(cumm):
        cumm[i] = n
        n += v
    perm = [0]*len(bwt)
    for i, v in enumerate(bwt):
        perm[cumm[v]] = i
        cumm[v] += 1

    i = perm[ptr]
    data = bytearray(len(bwt))
    for j in range(len(bwt)):
        data[j] = bwt[i]
        i = perm[i]
    return data




def main():
    start_timer = time.time()
    data = read_file(source_file)
    (transf, ponteiro) = EncodeBWT(data)
    run = rle_encode(transf)

    with open(destination_file + extension, 'wb') as f:
        f.write(run)
        f.close()
    print("Tempo de execução: " + str(round((time.time() - start_timer), 2)) + "s")



if __name__ == "__main__":
    main()
