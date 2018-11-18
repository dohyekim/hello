#encoding, #decoding

characterset
encoding

s = "한글"
print(len(s)) # >>> 2

bytes(s, 'UTF8')
s2 = bytes(s, 'UTF8')

print(len(s2)) # >>> 6  # UTF8에서는 한 글자가 3 byte


# ord() :문자를 숫자로 (ex.ascii code, utf8 code)
ord("a") #>> 97
ord("한") # >> 54620

bytearray(s, 'encoding')
bytearray("한글", "UTF8")
bytearray("한글", "EUC-KR")

# chr(97) → 'a', chr(65) → 'A'  :숫자를 문자로 
chr(i) 
