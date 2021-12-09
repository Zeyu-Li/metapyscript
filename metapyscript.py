import sys
import base64
import zlib

def main():
    if len(sys.argv) < 2:
        print("Provide the file to run as \nthe first argument when calling this script")
        return 

    code = ''
    try:
        code = sys.argv[1].split('.')[0].replace('_', '/').replace('-', '+')
    except:
        print("Could not file or open the script provided")
        return
    decompressed = ''
    try:
        decompressed = zlib.decompress(base64.b64decode(code.encode('ascii'))).decode('ascii')
    except:
        print("Could not decompress")
        return

    # print(decompressed)
    exec(decompressed)
    return 0

if __name__ == "__main__":
    main()
