<h1>Opis problemu:</h1>

3-partition problem, [wikipedia](https://en.wikipedia.org/wiki/3-partition_problem)

Problem 3-partycji jest problemem NP-zupełnym w informatyce.
Problem polega na tym, aby odpowiedzieć na następujące pytanie:

***Czy dany multizbiór liczb całkowitych można podzielić na "trojaczki", które mają taką samą sumę?***

> [!NOTE]
>- multizbiór różni się od zbioru tym, że w multizbiorze elementy mogą się powtarzać, a w zwykłym zbiorze nie
>- <code>trojaczki</code> - to trzy elementowe multizbiory
>- <code>n</code> - oznacza liczbę elementów w danym multizbiorze
>- <code>m</code> - oznacza liczbę "trojaczków", "koszyczków", "grup"
>- <code>T</code> - oznacza sumę wartości wszystkich elementów w multizbiorze
>- <code>S</code> - oznacza dany multizbiór
>- <code>S1, S2, …, Sm</code> - oznaczają "trojaczki", "pod-multizbiory"

> [!IMPORTANT]
>- <code>n</code> jest podzielne przez 3 oraz <code>n = 3m</code>
>- jeżeli <code>n</code> nie jest podzielne przez 3 to odpowiedź na pytanie przmi "nie"
>- elementy multizbioru to dodatnie liczby całkowite
>- <code>S1, S2, …, Sm</code> to multizbiory rozłączne pokrywające <code>S</code>

<h1>Przykłady:</h1>
<h2>Przykład 1)</h2>

> [!TIP]
>- Dany multizbiór: **S = {20, 23, 25, 30, 49, 45, 27, 30, 30, 40, 22, 19}**
>- Liczba elementów: **n = 12**
>- Liczba "trojaczków": **m = n/3 = 4**
>- Cel: **T = sum(S)/m = 360/4 = 90**
>- Odpowiedź: Tak
>- Pierwszy trojaczek: **S1 = {20, 25, 45}**
>- Drugi trojaczek: **S2 = {23, 27, 40}**
>- Trzeci trojaczek: **S3 = {49, 22, 19}**
>- Czwarty trojaczek: **S4 = {30, 30, 30}**

<h2>Przykład 2)</h2>
> [!TIP]
>- Dany multizbiór: **S = {1, 2, 5, 6, 7, 9}**
>- Liczba elementów: **n = 6**
>- Liczba "trojaczków": **m = n/3 = 2**
>- Cel: **T = sum(S)/m = 30/2 = 15**
>- Odpowiedź: Tak
>- Pierwszy trojaczek: **S1 = {1, 5, 9}**
>- Drugi trojaczek: **S2 = {2, 6, 7}**

<h2>Przykład 3)</h2>
> [!TIP]
>- Dany multizbiór: **S = {4, 5, 5, 5, 5, 6}**
>- Liczba elementów: **n = 6**
>- Liczba "trojaczków": **m = n/3 = 2**
>- Cel: **T = sum(S)/m = 30/2 = 15**
>- Odpowiedź: Tak
>- Pierwszy trojaczek: **S1 = {4, 5, 6}**
>- Drugi trojaczek: **S2 = {5, 5, 5}**

<h1>Komendy uruchamiające algorytmy:</h1>

Algorytm pełnego przeglądu:

<code>python -m cli brute -i data/input.txt</code>

Algorytm wspinaczkowy klasyczny z deterministycznym wyborem najlepszego sąsiada punktu roboczego:

<code>python -m cli hc_det -i data/input.txt --time-limit-seconds 5</code>

Algorytm wspinaczkowy z losowym wyborem sąsiada spośród otoczenia punktu roboczego:

<code>python -m cli hc_rand -i data/input.txt --time-limit-seconds 5</code>