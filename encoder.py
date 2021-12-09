import sys
import base64
import zlib


def main():
    if len(sys.argv) < 2:
        print("Provide the file to encode as \nthe first argument when calling this script")
        return 

    code = ''
    try:
        with open(sys.argv[1], 'r') as fp:
            code = ''.join(fp.readlines())
    except:
        print("Could not file or open the script provided")
        return
    
    # print(code)
    compressed = ''
    try:
        compressed = base64.b64encode(zlib.compress(code.encode('ascii'))).decode('ascii').replace('/', '_').replace('+', '-')
    except:
        print("Could not compress")
        return

    try:
        file_name = f'{compressed}.metapy'
        with open(file_name, 'w'): pass
        print(f"Wrote to {file_name}")
    except:
        print("Could write file")
        return
    

    return 0

if __name__ == "__main__":
    main()
