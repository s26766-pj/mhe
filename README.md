<h2>Spis treści:</h2>

- [ Opis problemu ](#desc)
- [ Przykłady: ](#examples)
  - [ przykład 1 ](#example1)
  - [ przykład 2 ](#example2)
  - [ przykład 3 ](#example3)
- [ Komendy wywołujące: ](#usage)
  - [ algorytm pełnego przeglądu ](#usage1)
  - [ algorytm wspinaczkowy klasyczny ](#usage2)
  - [ algorytm wspinaczkowy z losowym wyborem sąsiada ](#usage3)
  - [ algorytm tabu ](#usage4)
  - [ algorytm symulowanego wyżarzania ](#usage5)

<a name="desc"></a>
## Opis problemu:

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

<a name="examples"></a>
## Przykłady:
<a name="example1"></a>
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

<a name="example2"></a>
<h2>Przykład 2)</h2>

> [!TIP]
>- Dany multizbiór: **S = {1, 2, 5, 6, 7, 9}**
>- Liczba elementów: **n = 6**
>- Liczba "trojaczków": **m = n/3 = 2**
>- Cel: **T = sum(S)/m = 30/2 = 15**
>- Odpowiedź: Tak
>- Pierwszy trojaczek: **S1 = {1, 5, 9}**
>- Drugi trojaczek: **S2 = {2, 6, 7}**

<a name="example3"></a>
<h2>Przykład 3)</h2>

> [!TIP]
>- Dany multizbiór: **S = {4, 5, 5, 5, 5, 6}**
>- Liczba elementów: **n = 6**
>- Liczba "trojaczków": **m = n/3 = 2**
>- Cel: **T = sum(S)/m = 30/2 = 15**
>- Odpowiedź: Tak
>- Pierwszy trojaczek: **S1 = {4, 5, 6}**
>- Drugi trojaczek: **S2 = {5, 5, 5}**

<a name="usage"></a>
## Komendy uruchamiające algorytmy:

> [!NOTE]
> - parametr <code>-m cli <nazwa_algorytmu></code> ustala wybranie algorytmu
> - parametr <code>-i <nazwa_pliku_tekstowego></code> ustala wybranie pliku tekstowego z elementami multizbioru

<a name="usage1"></a>
## Algorytm pełnego przeglądu:

<code>python -m cli brute -i data/p1.txt</code>

<a name="usage2"></a>
## Algorytm wspinaczkowy klasyczny z deterministycznym wyborem najlepszego sąsiada punktu roboczego:

<code>python -m cli hc_det -i data/p1.txt --time-limit-seconds 5</code>
> [!NOTE]
> - parametr <code>--time-limit-seconds <int></code> ustala czasowe ograniczenie działania algorytmu

<a name="usage3"></a>
## Algorytm wspinaczkowy z losowym wyborem sąsiada spośród otoczenia punktu roboczego:

<code>python -m cli hc_rand -i data/p1.txt --time-limit-seconds 5</code>
> [!NOTE]
> - parametr <code>--time-limit-seconds <int></code> ustala czasowe ograniczenie działania algorytmu

<a name="usage4"></a>
## Algorytm tabu:

<code>python -m cli tabu -i data/p1.txt --tabu-size 0 --time-limit-seconds 5</code>
> [!NOTE]
> - parametr <code>--time-limit-seconds <int></code> ustala czasowe ograniczenie działania algorytmu
> - parametr <code>--tabu-size <int></code> ustala ograniczenie wielkości tabu, gdy podamy 0 tabu jest nieograniczone

<a name="usage5"></a>
## Algorytm symulowanego wyżarzania:

<code>python -m cli sa -i data/p1.txt</code>

<code>python -m cli sa -i data/p1.txt --schedule exponential --alpha 0.97 --sigma 0.5 --time-limit-seconds 10</code>

<code>python -m cli sa -i data/p1.txt --schedule logarithmic --c 2.0 --time-limit-seconds 60</code>

<code>python -m cli sa -i data/p1.txt --schedule linear --initial-temp 100.0 --alpha 0.5 --sigma 0.8 --time-limit-seconds 120</code>
> [!NOTE]
> - parametr <code>--schedule <nazwa_schematu_temperatury></code> ustala schemat wyżarzania, może być liniowy, wykładniczy lub logarytmiczny (<code>linear, exponential, logarithmic</code>)
> - parametr <code>--alpha <float></code> w schematach liniowym i wykładniczym ustala tempo spadku temperatury
> - parametr <code>--c <float></code> w schemacie logarytmicznym ustala tempo spadku temperatury
> - parametr <code>--initial_temp <float></code> ustala temperaturę początkową
> - parametr <code>--sigma <float></code> ustala odchylenie standardowe wyborze sąsiada
> - parametr <code>--time-limit-seconds <int></code> ustala czasowe ograniczenie działania algorytmu


