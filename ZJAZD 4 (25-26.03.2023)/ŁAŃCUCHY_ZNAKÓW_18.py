# ŁAŃCUCHY ZNAKÓW

# lista l = [1, 2, 3] - list -- lista charaktyryzuje się, że do elementów odwujemy sie za pomocą indeksów, jest mutowalna
# krotka t = (1,2,3) (ang. tuple) - tuple -- także charaktyryzuje się, że do elementów odwujemy sie za pomocą indeksów, ale nie jest mutowalna
# słownik d = {"a":1, "b":2} - dictionary -- słownik nie jest sekwencją, czyli nie możemy po nim przejść pętlą. Elementy są uporządkowane.
# ciąg znaków s = "asas" - string -- trochę podobny do krotki, mozna po nim iterować, ale jest niemutowalny


# txt = "Ala ma kota" # mmozna dac cudzysłów ", ale też może byc też apostrof '
#
# print(txt)
# print(txt[-1])
# print(len(txt))
# print(len(""))
#
# print (len("\t\n\\")) # ciąg znaków o długości

# wieloliniowe łancuchy znaków
# txt = "To jest tekst" \
#       "to dalszy ciąg"
# print(txt)

# lub

# txt = """To jest tekst"
#       to dalszy ciąg"""
# print(txt)

# lub

# txt = """Aa
# b
# c"""
# txt2 = "a\nb\nc"
#
# print(len(txt))
# print(len(txt2))
#
# print(txt)

# ------- KONKATENACJA + REPLIKACJA -- CIAGÓW ZNAKÓW
# str1 = "a"
# str2 = "b"
#
# print(str1 + str2)
# print(str2 + str1)
# print()
# print(str1 * 3)
# print(5 * str2)
#
# # operator skrótów
# str1 += str2 # to jest ab - dodawania
# print(str1)
#
# str1 *= 10 # replikacja=mniozeni
# print(str1)



##-------------KODOWANIE------

# char1 = "a" # znak a
# char2 = " "
#
# print(ord(char1))# Wyswietl mi punkt kodowy dla znaku pierwszego, czyli 'a' - to jest nr 97
# print(ord(char2))# dla spacji to numer 32
#
# # www.asciitable.com --> strona internetowa z tabelą ASCII
#
# print(ord("ę")) # punkt kodowy dla literki ę, to 281
# print(hex(ord("ę"))) # teraz mamy wartość heksadecymalną
#
#
# print("\u0119") # nA bazie kodu UniCode generujemy literkę ę



#---KODOWANIE UTF8

# c = "a"
# print(c)
# print(c, ord(c), hex(ord(c)), c.encode()) # generalne dane dla litery a
#
# print()
#
# c = "\u20AC" # to jest numer w unikode dla znaczka euro
# print(c)
# print(c, ord(c), hex(ord(c)), c.encode()) # generalne dane dla znaczka euro


#----FUNKCJA CHR

# print(chr(97)) # znak a
# print(chr(945)) # znak alfa
#
# print("a" == chr(ord("a")))

#---ŁANCUCH ZNAKÓW JAkO SEKWENCJA

# ten teks jest indeksowany
    #    0123456789
# txt = "Ala ma kota"
#          ...-4-3-2-1
# print(txt[2]) # wyswietlamy a
# print(txt[-3]) # wyswietlamy o

# for c in range (len(txt)):
#     print(txt[c], end=" ")

    # lub

# for i in range (len(txt)):
#     print(txt[i], end="-")
# print()
#
# for c in txt:
#     print(c, end="-")


# -----WYCINKI
      # 0123456789
# txt = "Ala ma kota"
#
# print(txt[4:6])
# print(txt[7:])
# print(txt[-1:])
# print(txt[2::3])


# ----Generujemy alfabet bez polskich znaków
# print(ord("a"))
# print(ord("z"))

# for i in range (ord("a"), ord("z") + 1 ):
#     print(chr(i), end="")


#----------
# alphabet = ""
# for i in range (ord("a"), ord("z") + 1 ):
#     alphabet += chr(i)
# print(alphabet)
#
# #---------
# alphabet = ""
# for i in range (ord("a"), ord("z") + 1 ):
#     alphabet += chr(i)
# print(alphabet)
#
# print("a" in alphabet)
# print("A" in alphabet)
# print("abce" in alphabet)
# print("abc" in alphabet)

#-----niemutowalnosc ciagów znaków
# alphabet = ""
# for i in range (ord("a"), ord("z") + 1 ):
#     alphabet += chr(i)
# print(alphabet)
# del alphabet[0] # nie mozna usunac pojedynczych znaków, bo ciag znaków jest niemutowaly

# del alphabet
# print(alphabet) # teraz usunąłemcały alfavbet
#
# alphabet.append("asdasd") # nie mozna nic dodac
# alphabet.insert("asdasd") # nie mozna nic dodac

# alphabet += "AAAA"
# print(alphabet)

#------
# alphabet = ""
# for i in range (ord("a"), ord("z") + 1 ):
#     alphabet += chr(i)
# # print(min([1,2,3]))
#
# print(min("abcABC"))
# print(max("abcABC"))
#
#
# print(max("Ala ma kota"))

#---FUNKCJA INDEKS

# print(alphabet.index("w")) # jaki ma indeks literka w = 22
#
# print("aAbByYzZAa".index("A")) # mam wartosc 1 - funkcja ineks zrwaca inkeks ierwszego wystapienia, tak ze dlatego rtaz tą jedynkę wyswietliło
# print("aAbByYzZAa".index("ZA"))
#
# print([1,2,3].index(3))
#
# # --- Funkcja List
# print(list(alphabet))
#
# print(alphabet.count("a"))
# print("Ala ma kota".count("a"))
#
# print([1,1,2,2,4].count(1))

# ---szyfr cezara
# ABCDEFG # szyfr cezara z przesunieceim trzy, to mamy wtedy
#    ABCD # tu mamy to przesunięcie
# XYZ