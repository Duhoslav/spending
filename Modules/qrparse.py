
def qrparse(qrstr):
    try:
        list = qrstr.split('&')

        if 'fn=' in list[2]:
            fn = list[2].strip('fn=')
            print(fn)
            if 'i=' in list[3]:
                fd = list[3].strip('i=')
                print(fd)
                if 'fp=' in list[4]:
                    fp = list[4].strip('fp=')
                    print(fp)

                    return fn, fd, fp
    except Exception as e:
        print(e)
