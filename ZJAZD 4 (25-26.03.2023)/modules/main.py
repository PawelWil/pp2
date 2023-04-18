import module
# tu na bazie danych w module o nazwie 'module' możemy poprzez funkcję import wyciągnąć poszczególne dane, jak ponizej:

# print (dir(module)) # sprawdzamy co w sobie zawiera moduł 'module'
# help (module) # teraz używamy funckji help

# teraz korzystamy z użytej logiki w tym module 'module', która tam została napisana, a jest użyta w innym skrypcie, po to żeby jej już nie
# tworzyć ponownie, ale wykorzystać w tym skrypcie i wielu innych
print ("Czy to jest ciąg znaków? ", module.is_string("test")) # tu sprawdzamy czy to jest ciąg znaków, czy nie. Jesli tak, to będzie TRUE
print("suma elementów listy:", module.sum_list_elem([3,4,2,1,2,4,5])) # a tu sprawdzamy sume elemntów z listy