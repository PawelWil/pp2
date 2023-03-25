import MODUŁY_16 # wazna rzecz ! tu zeby zaimportowac ten moduł stworzony przeze mnie, muszę się odnieść do dokłądnej nazwy katalogu, gdzie go stworzyłem,
# czyli w moim przypadku to 'MODUŁY_16' i dlatego poniżej odnoszę się do tej nazwy

print ("Czy to jest ciąg znaków? ", MODUŁY_16.is_string("test"))
print("suma elementów listy: ", MODUŁY_16.sum_list_elem([3,4,2,3,1]))

# ---- teraz ten modul, który stworzylismy chcemy uzyc
# import module # coś nie dziala...
# print (dir(module))
# help(module)

# import module
#
# print ("Czy to jest ciąg znaków? ", module.is_string("test"))
# print("suma elementów listy: ", module.sum_list_elem([3,4,2,3,1]))