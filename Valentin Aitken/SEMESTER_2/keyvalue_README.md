Да се реализира REST услуга която да използва API-тата на NCBI за извличане на материали от базата им данни PubMed. 
REST услугата трябва да предоставя възможност за търсене по заявка и запазване на резултатите в база данни.

Поради лимитацийте на PubMed не могат да се извършват неограничен брой операции към публичните API-та. 
Необходимо е да се изгради кеширащ механизъм за да се запазват предходните извиквания и по този начин да се 
намалят реалните обръщения към вътрешната база и NCBI API/s.

За изграждането на REST услугата е препоръчително да се използват поне 2 бази данни. Една за съхранение на резултатите върнати от NCBI PubMed API-тоз
и друга за изграждане на кеширащ механизъм.

Да интегрирам reutils с новия кеш.

redis short cache

db cache

https://www.ncbi.nlm.nih.gov/books/NBK25497/

NCBI API за търсене на резултати по критерии
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=science%5bjournal%5d+AND+breast+cancer+AND+2008%5bpdat%5d

NCBI API за извличане на целия документ
https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&id=19008416

Документация на NCBI PubMed API
https://www.ncbi.nlm.nih.gov/books/NBK25500/#chapter1.Searching_a_Database

etcd key value DB 
https://buildmedia.readthedocs.org/media/pdf/etcd/latest/etcd.pdf
https://etcd.io/docs/v3.3.12/learning/client-architecture/