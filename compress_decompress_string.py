import zlib


def main():
    str = "hello world!hello world!hello world!hello world!".encode()
    compress_str = zlib.compress(str)
    print('Compressed string:', compress_str)
    decompressed_str = zlib.decompress(compress_str)
    print('Decompressed string:', decompressed_str)


main()