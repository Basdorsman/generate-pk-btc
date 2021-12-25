import hashlib
import binascii # importing binascii to be able to convert hexadecimal strings to binary data
import base58

def convert_raw_to_wif(raw):
	extended_key = "80"+raw
	first_sha256= hashlib.sha256(binascii.unhexlify(extended_key)).hexdigest()
	second_sha256 = hashlib.sha256(binascii.unhexlify(first_sha256)).hexdigest()
	final_key = extended_key+second_sha256[:8]
	wif = base58.b58encode(binascii.unhexlify(final_key))
	return wif


