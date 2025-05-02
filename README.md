<h1>Opis problemu:</h1>

3-partition problem, [wikipedia](https://en.wikipedia.org/wiki/3-partition_problem)

Problem 3-partycji jest problemem NP-zupełnym w informatyce.
Problem polega na tym, aby zdecydować, czy dany zbiór liczb całkowitych można podzielić na trzy partycje "wiadereka", tak aby w każdym wiaderku była taka sama suma?

Przykład:

Zbiór: **S = {7, 3, 2, 1, 5, 4, 8}**

Suma liczb w zbiorze **S = 30**

Docelowa suma w każdej partycji **30 / 3 = 10**

Rozwiązanie:

Partycja 1: {7, 3} (Suma = 10)

Partycja 2: {5, 4, 1} (Suma = 10)

Partycja 3: {8, 2} (Suma = 10)

<h1>Komendy uruchamiające algorytmy:</h1>

Algorytm pełnego przeglądu:

<code>python -m cli brute -i data/input.txt</code>

Algorytm wspinaczkowy klasyczny z deterministycznym wyborem najlepszego sąsiada punktu roboczego:

<code>python -m cli hc_det -i data/input.txt --time-limit-seconds 5</code>

Algorytm wspinaczkowy z losowym wyborem sąsiada spośród otoczenia punktu roboczego:

<code>python -m cli hc_rand -i data/input.txt --time-limit-seconds 5</code>