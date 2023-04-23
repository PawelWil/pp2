# tu dokonujemy importu modułu 1 z package1, i tak samo dla modułu 2
from package1 import module1
from package1 import module2

#teraz wywołujemy funkcję 'introduce' z modułu 1 + funkcję 'introduce' z modułu 2, zawartych w pakiecie 'package 1'
module1.introduce()
module2.introduce()

# jak widać wyswietliło się wszystko zarowno z module1, module2 jak i pliku __init__, czyli:
#####################
# Pakiety są super#
#####################
#Jestem fukncją z modułu package1.module1
#Cześć, Jestem fukncją z modułu package1.module2
