Problem chińskiego listonosza (ang. Chinese postman problem)

Dlaczego listonosza ?
W swojej pracy, listonosz wyrusza z poczty, dostarcza przesyłki adresatom, by na koncu powrócić na pocztę. Aby wykonać swoją pracę musi przejść po każdej ulicy w swoim rejonie co najmniej raz. Oczywiście chciałby, aby droga, którą przebędzie, była możliwie najkrótsza.

Dlaczego chińskiego ?
Problem ten został sformułowany po raz pierwszy w języku teorii grafów przez chinskiego matematyka Mei Ku Kwana w 1962 roku.

Sformułowanie problemu.
Rozważmy graf, którego krawędzie odpowiadają ulicom w rejonie, obsługiowanym przez listonosza. Wierzchołki to po prostu skrzyżowania ulic. Krawędziom nadajemy wagi, które oznaczają odległości między dwoma skrzyżowaniami. Znalezienie możliwie najkrótszej drogi, którą musi przejść listonosz sprowadza sie do znalezienia w tym grafie drogio minimalnej sumie wag krawędzi, która przechodzi przez każdą krawędź co najmniej raz.

Jeśli graf posiada cykl Eulera.
Jeśli dany graf posiada cykl Eulera, to istnieje taka droga, która zaczyna i konczy sie w tym samym punkcie i wymaga przejścia po każdej ulicy dokładnie raz. Zauważmy, że ponieważ każdy cykl Eulera przechodzi raz przez każdą krawędź to suma wag krawędzi (długość drogi, którą musi przejść listonosz) jest zawsze taka sama (nie zależy od wierzchołka, w którym cykl ten zaczyna się i konczy). Rozwiązaniem jest więc dowolny cykl Eulera w tym grafie.

Jeśli graf nie posiada cyklu Eulera.
W takim przypadku listonosz będzie zmuszony przejść niektórymi ulicami wielokrotnie. Rozwiązanie jest więc cyklem, w którym suma długości krawędzi wybranych więcej niż raz jest możliwie najmniejsza.