import argparse

from lz import *


NESTROID_EMULATOR_ADDR_REL = 0xB2 + 0x2AE
NESTROID_EMULATOR_DECOMP_SIZE = 0x8574


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("binjp_path", type=str, help="Path to built emulator binary")
    parser.add_argument("output_path", type=str, help="Path where output emulator data should be written")
    
    args = parser.parse_args()
    
    with open(args.binjp_path, "rb") as f:
        f.seek(NESTROID_EMULATOR_ADDR_REL)
        data = f.read()
    
    decomp_data, comp_len = decomp_lz_custom(data, 0, NESTROID_EMULATOR_DECOMP_SIZE)
    print(comp_len)
    
    with open(args.output_path, "wb") as f:
        f.write(decomp_data)
    
