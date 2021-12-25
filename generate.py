import blocksmith
import sys
from convert_wif import convert_raw_to_wif

kg = blocksmith.KeyGenerator()


kg.seed_input(sys.argv[1])
key = kg.generate_key()
print(f'private key: {key}')

address = blocksmith.BitcoinWallet.generate_address(key)
print(f'address: {address}')

wif=convert_raw_to_wif(key)
print(f'wif: {wif}')
