
# tu robimy import, ale z wykorzystaniem aliasów
# czyli z pakietu 'package1', z modułu 'module1' zaimportuj funkcję 'introduce', i zaaliasuj go (zmień nazwę) jako funkcja 'i1'
# i dokładnie to samo dla modułu 'module2'
from package1.module1 import introduce as i1
from package1.module2 import introduce as i2

#Dzięki aliasowaniu, możemy rozróżnić 2 funkcje 'introduce' zawarte w modułach (module1 i module2), które to funkcje
#maję tą samą nazwę, czyli jeśli dwa razy wpiszę 'introduce', druga nadpisze pierwszą, zaś jak zaaliasuje jako i1 + i2, to
# już nie ma możliwości żeby pierwsza nadpisała drugą, bo mają dwie różne nazwy
i1() # to już po zaaliasowaniu jest dla funkcji introduce z module 1
i2() # to już po zaaliasowaniu jest dla funkcji introduce z module 2

# teraz wywołujemy funkcję 'dir', która wyswietla bieżącą przestrzeń nazw, do czego mamy dostęp w tym pliku, gdzie jak widać,
# mamy dostęp do właściwości name, pakietu package i funkcji i 1 oraz i2
print(dir())
