# napisac program jak zaszyfrować coś
# szyfrujemy  znakami: Xq|'gf(bm{|(nibfg)
# dla każdego znaku zmieniono 4=czwarty bit na przeciwny
# bity liczymy od najmniej znaczącego, 4 bit(czwarty) -> indeks 3

#wyswietlanie znaków
  # wyświetlamy znak c
# print("c") # najprostze wyswietlenie jakiegos znaku
#
# print(ord("c")) # ta funkcja ma wartosc w tabeli ASCii (tu jest 99) i ta funkcja ORD nam o tym mowi
# print(bin(ord("c"))) # rozpisanie jak to wygląda binarnie
#
# print(chr(99)) # tu dostajemy co pod tym kodem ASCII się kryje - robimy to za pomocą funkcji CHR

# --Przykład zamiany bitów:
# print("{:08b}".format(ord("c"))) # to jest 01100011
   # chcemy to 01100011 zmienic na 01101011
# 01100011 - to jest nasza liczba
# 00001000 - to jest maska, za pomocą której powyższą liczbe maskujemy
# 01101011 - to jest za pomocą 'exor'- alternatywy rozłącznej, czyli zamiany bitów na przeciwne, ale tylko bitów, które wskażemy za pomoca powyższej maski

# print("{:08b}".format(1<<3)) # to jest nasza maska (tu podczas tworzenia maski tez pokazuje jak sie przesuwa bity)
# print("{:08b}".format(ord("c") ^ (1<< 3))) # to już jest finalny skutek

# print(chr(ord("c") ^ ( 1 << 3))) # to jest cyfra k

msg = "Xq|'gf(bm{|(nibfg)"
for c in msg: # biore kazde z nas ze zmeinneg msg
# print(c) # tu sobie zobaczę, ze ten ciag znaków z msg jest widoczny
    print(chr(ord(c) ^ (1 << 3)), end="")