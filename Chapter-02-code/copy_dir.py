import os
import sys
maxfileload = 1000000
blksize = 1024 * 50


def copyfile(pathFrom, pathTo, maxfileload=maxfileload):
    """
   Copy files from pathFrom to pathTo byte by byte, read and write using binary mode
    """

    if os.path.getsize(pathFrom) <= maxfileload:
        bytesFrom = open(pathFrom, 'rb').read()
        open(pathTo, 'wb').write(bytesFrom)
    else:
        fileFrom = open(pathFrom, 'rb')
        fileTo = open(pathTo, 'wb')
        while True:
            bytesFrom = fileFrom.read(blksize)
            if not bytesFrom:
                break
            fileTo.write(bytesFrom)

def copytree(dirFrom, dirTo, verbose=0):
    """
    Copy directory
    """
    fcount = dcount = 0
    for filename in os.listdir(dirFrom):
        pathFrom = os.path.join(dirFrom, filename)
        pathTo = os.path.join(dirTo, filename)
        if not os.path.isdir(pathFrom):
            try:
                if verbose > 1:
                    print("copy", pathFrom, "to", pathTo)
                copyfile(pathFrom, pathTo)
                fcount += 1
            except:
                print("copy error", pathFrom, "to", pathTo)
        else:
            if verbose:
                print('copying dir', pathFrom, 'to', pathTo)
            try:
                os.mkdir(pathTo)  # create a subdirectory
                below = copytree(pathFrom, pathTo, verbose) 
                fcount += below[0]
                dcount += below[1]
                dcount += 1
            except:
                print("create error", pathFrom, "to", pathTo)
                print(sys.exc_info()[0], sys.exc_info()[1])
    return fcount, dcount


if __name__ == "__main__":
    dirForm = r"d:\BaiduYunDownload"
    dirTo = r"d:\BaiduYunDownload.bak"
    os.mkdir(dirTo)
    fcount, dcount = copytree(dirForm, dirTo, verbose=2)
    print("copy directory: %d;copy file: %d" % (fcount, dcount))



