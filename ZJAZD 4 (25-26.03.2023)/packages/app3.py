# teraz będziemy robić import pakietu, z całkowicie innej ścieżki = poza naszym projektem pycharmowym,
# czyli np. z pulpitu naszego komputera. Szybki skrót do pulpitu
# to przycisk ' znaczek win' + d. Czyli kopiujemy sobie pakiet 'package1'- najeżdzamy na niego kursorem - prawy myszki - kopiuj -
# paste na pulpicie - zmieniamy jego nazwę już na pulpicie, na 'package2_'

# import czegoś z zewnątrz, robimy za pomocą modułu systemowego 'sys' oraz podaniu konkretnej ścieżki, gdzie ten plik się znajduje
import sys

# dla tego modułu 'sys' wywołujemy funkcję = obiekt 'path', do którego za pomocą funkcji 'append' dodajemy odpowiednią ścieżkę, w  momencie
# gdy będziemy chcieli coś dopimportować - tu musimy wskazać ścieżkę, gdzie mają być szukane nasze moduły, i robię to w następujący sposób:
# otwieram katalog 'Moj Komputer' - następnie wchodzę w 'pulpit' - wchodzę w plik 'package2_' - wyświetla mi się całaścieżka z 'package2' -
# ale ten 'package2_' z tej ściezki usuwam i dostaję: C:\Users\Dell\OneDrive\Desktop - teraz zaznaczam tą ścieżkę i ją kopuiję -
# i wklejam poniżej, ale BARDZO WAŻnA RZECZ: jak już skopiuję, może dodać po jednym backslashu, do koażdego istniejącego packslashu,
# bo Python jak jest jeden Windowsowy backslash nie odczytuje tej ściezki - więc nasza scieżka będzie wyglądać następująco:
# C:\\Users\\Dell\\OneDrive\\Desktop - i taki link dodajemy poniżej.
# Kolejna WAZnA Rzecz to jest to, że nawet jak ściezka jest poprawna to nasz IDLE 'Pycharm' pokazuje ze niby jest to błąd, ale jest ok
# czyli na spokoju się połączymy z pakietem 'package2_' i jesteśmy w stanie wyswieltlić co tam jest
sys.path.append("C:\\Users\\Dell\\OneDrive\\Desktop")

# tu już po podaniu ściezki zaimportowaliśmy sobie 'package2_' i module 1
from package2_ import module1

# tu wyswietlamy funkcję introduce z module 1
module1.introduce()

# jak widać wyswietliło się wszystko zarowno z module1, module2 jak i pliku __init__, czyli:
# ale tez wazne bo dlatego, że wszystkie te 3 pliki nie zostały zmienione, zostały skopiowane 1 do 1

#####################
# Pakiety są super#
#####################
#Jestem fukncją z modułu package1.module1
#Cześć, Jestem fukncją z modułu package1.module2




