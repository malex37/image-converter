from base64converter import Base64Converter
import argparse
# make it simple just invoke base64 by default
argumentPurser = argparse.ArgumentParser("simple_example")
argumentPurser.add_argument('args_print', help="prints the arguments back to you")
args = argumentPurser.parse_args()
print(args)
encoded_image = Base64Converter('./spooder.jpg').encode()
print(encoded_image)