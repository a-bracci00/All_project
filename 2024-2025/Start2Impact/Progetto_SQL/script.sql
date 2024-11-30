/*
SCHEMA CREAZIONE TABELLA data_2023
Se non esiste crea la tabella data_2023
*/
CREATE TABLE IF NOT EXISTS data_2023 (
	Country VARCHAR(255),
	Density INTEGER,
	Abbreviation VARCHAR(255),
	Agricultural_Land NUMERIC,
	Land_Area NUMERIC,
	Armed_Forces_size INTEGER,
	Birth_Rate NUMERIC,
	Calling_Code INTEGER,
	Capital_Major_City VARCHAR(255),
	Co2_Emissions INTEGER,
	CPI NUMERIC,
	CPI_Change NUMERIC,
	Currency_Code VARCHAR(255),
	Fertility_Rate NUMERIC,
	Forested_Area NUMERIC,
	Gasoline_Price NUMERIC,
	GDP BIGINT,
	Gross_primary_education_enrollment NUMERIC,
	Gross_tertiaryeducation_enrollment NUMERIC,
	Infant_mortality NUMERIC,
	Largest_city VARCHAR(255),
	Life_expectancy NUMERIC,
	Maternal_mortality_ratio INTEGER,
	Minimum_wage NUMERIC,
	Official_language VARCHAR(255),
	Out_of_pocket_health_expenditure NUMERIC,
	Physicians_per_thousand NUMERIC,
	Population INTEGER,
	Population_Labor_force_participation NUMERIC,
	Tax_revenue NUMERIC,
	Total_tax_rate NUMERIC,
	Unemployment_rate NUMERIC,
	Urban_population INTEGER,
	Latitude NUMERIC,
	Longitude NUMERIC
);

/*
SCHEMA CREAZIONE TABELLA global_data
Se non esiste crea la tabella global_data
*/	
CREATE TABLE IF NOT EXISTS global_data (
	Entity	VARCHAR(255),
	Year	INTEGER,
	Access_to_electricity NUMERIC,
	Access_to_clean_fuels_for_cooking NUMERIC,
	Renewable_electricity_generating_capacity_per_capita NUMERIC,
	Financial_flows_to_developing_countries BIGINT,
	Renewable_energy_share_in_the_total_final_energy_consumption NUMERIC,
	Electricity_from_fossil_fuels NUMERIC,
	Electricity_from_nuclear NUMERIC,
	Electricity_from_renewables NUMERIC,
	Low_carbon_electricity NUMERIC,
	Primary_energy_consumption_per_capita NUMERIC,
	Energy_intensity_level_of_primary_energy NUMERIC,
	Value_co2_emissions_kt_by_country NUMERIC,
	Renewables NUMERIC,
	gdp_growth NUMERIC,
	gdp_per_capita NUMERIC,
	Density INTEGER,
	Land_Area INTEGER,
	Latitude NUMERIC,
	Longitude NUMERIC
);

-- Ritorna tutte le colonne di data_2023 per controllare
-- che sia tutto corretto
SELECT *
FROM data_2023;

-- Ritorna tutte le colonne di global_data per controllare
-- che sia tutto corretto
SELECT *
FROM global_data;

-- Ritorna la colonna country dalla tabella data_2023 per visualizzare i paesi
SELECT country
FROM data_2023;

/* 
Cambio il nome della colonna "Entity" (se esiste) nella tabella global_data
con "Country", cosicchè da avere un'altra colonna combaciante di nome tra le due tabelle in vista
di una futura join, rendendola anche più semplice da capire
*/
DO $$
BEGIN
	IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'global_data' AND column_name = 'Entity') THEN
		ALTER TABLE global_data RENAME Entity TO Country;
	END IF;
END$$;

/*
Cambio il nome della colonna "year" (se esiste) (nome non modificato nella creazione della tabella proprio per questo) in year_ 
per evitare di usare parole che facciano riferimento a funzioni già esistenti
*/
DO $$
BEGIN
	IF EXISTS (SELECT 1 FROM information_schema.columns WHERE table_name = 'global_data' AND column_name = 'year') THEN
		ALTER TABLE global_data RENAME year TO year_;
	END IF;
END$$;

/*
Quale paese ha una densità (P/km2) più alta?
Seleziono il paese e la densità della popolazione per (P/km2) con il valore più grande
*/
SELECT country, density
FROM data_2023
WHERE density = (SELECT MAX(density) 
				 FROM data_2023);

/*
Seleziono ogni paese ed il corrispettivo valore di densità (P/km2) per confrontarlo 
con il valore massimo trovato nella colonna densità
*/
SELECT country, density, MAX(density) OVER() 
FROM data_2023;

/*
Quali sono le capitali di ciascun paese?
Seleziono ogni paese e la rispettiva capitale
*/
SELECT country, capital_major_city
FROM data_2023;

/*
Seleziono i vari paesi e le varie capitali con i relativi dati sulla densità, sulle emissioni
di co2 in tonnellate e sul costo della benzina in dollari
*/
SELECT country, capital_major_city, density, co2_emissions, gasoline_price
FROM data_2023;

/*
Quali sono i paese con il valore di co2 dal più basso al più alto?
Seleziono la capitale, il paese ed il valore emissione CO2, dove il valore non sia NULL
raggruppando i valori in un ordine specifico ordinandoli dal valore più piccolo
*/
SELECT capital_major_city, country, co2_emissions
FROM data_2023
WHERE co2_emissions IS NOT NULL
ORDER BY co2_emissions;

/*
Aggiungo i valori delle capitali dove mancanti
*/
UPDATE data_2023
SET capital_major_city = 'Tripoli'
WHERE country = 'Libya';

UPDATE data_2023
SET capital_major_city = 'Singapore'
WHERE country = 'Singapore';

/*
Elimino la riga che ha come paese "Palestinian National Authority" 
perchè priva o carente di dati utilizzabili
*/
DELETE FROM data_2023
WHERE country = 'Palestinian National Authority';

/*
Controllo che sia stata eliminata a dovere
*/
SELECT country
FROM data_2023
WHERE country = 'Palestinian National Authority';

/*
Quali sono i paesi più inquinanti?
Seleziono i 3 paesi con più emissione CO2, dove il valore non sia NULL
raggruppando i valori e ordinandoli in modo decrescente
*/
SELECT country, co2_emissions
FROM data_2023
WHERE co2_emissions IS NOT NULL
ORDER BY co2_emissions DESC
LIMIT 3;

/*
Creazione una vista denominata avg_co2emissions (se non esite già) che contiene il valore medio delle emissioni di co2 
denominato co2_mean
*/
DO $$
BEGIN
	IF NOT EXISTS (SELECT 1 FROM pg_views WHERE viewname = 'avg_co2emissions') THEN
		EXECUTE 'CREATE VIEW avg_co2emissions AS 
					 SELECT CAST(AVG(co2_emissions) AS INT) AS co2_mean
					 FROM data_2023';
	END IF;
END$$;

/*
Controllo se il valore della vista precedente corrisponde alle mie aspettative
*/
SELECT *
FROM avg_co2emissions;

/*
Come sono messi i paesi in base al valore medio di co2?
Seleziono i paesi e le corrispondenti emissioni confrontando quest'ultime con il valore medio
preso dalla vista creata precedentemente creando una nuova colonna denominata 'level_co2',
che in base al soddisfacimento di determinate condizioni assegna un valore a 'level_co2'
nella corrispettiva riga
*/
SELECT country, co2_emissions, 
	CASE
		WHEN co2_emissions < (SELECT co2_mean from avg_co2emissions) THEN 'Lower than average'
		WHEN co2_emissions > (SELECT co2_mean from avg_co2emissions) THEN 'Higher than average'
		ELSE 'Equal to the average'
	END AS Level_CO2
FROM data_2023;

/*
Quanti sono i paesi con un valore di co2 con un livello sopra, sotto o uguale alla media?
Ricopiando la query sopra e utilizzandola come se fosse una tabella, 
conto il totale dei paesi e quanti hanno le emissioni di co2 sopra, sotto o uguale alla media
*/
SELECT
	COUNT(1) AS Totale,
	SUM(CASE WHEN level_co2 = 'Lower than average' THEN 1 ELSE 0 END) AS Lower_than_average,
	SUM(CASE WHEN level_co2 = 'Higher than average' THEN 1 ELSE 0 END) AS Higher_than_average,
	SUM(CASE WHEN level_co2 = 'Equal to the average' THEN 1 ELSE 0 END) AS Equal_than_average
FROM 
	(SELECT country, co2_emissions, 
		CASE
			WHEN co2_emissions < (SELECT co2_mean from avg_co2emissions) THEN 'Lower than average'
			WHEN co2_emissions > (SELECT co2_mean from avg_co2emissions) THEN 'Higher than average'
			ELSE 'Equal to the average'
		END AS Level_CO2
	 FROM data_2023);

/*
Nel corso degli anni, la popolazione ha avuto un miglioramento per l'accesso all'energia elettrica? Si
Seleziono dalla tabella data_2023 i paesi, e da global_data
gli anni dal 2000 al 2020 di ogni paese e la percentuale di persone con accesso all'elettricità utilizzando 
un inner join così da avere solo le righe in comune tra le due tabelle in base ai
valori contenuti nella colonna country, per avere un idea chiara sul progresso o regresso
sull'accesso all'elettricità negli anni e la velocità con cui è avvenuto
*/
SELECT d.country, g.year_, g.access_to_electricity
FROM data_2023 d
INNER JOIN global_data g
ON d.country = g.country;

/*
Stessa cosa di sopra ma scritta in maniera diversa
*/
SELECT d.country, g.year_, g.access_to_electricity
FROM data_2023 d, global_data g
WHERE d.country = g.country;

/*
Quante e che tipi di risorve vengono utilizzate per generare energia in ogni singolo paese? C'è stata una differenza in 20 anni?
Seleziono il paese, l'anno, l'elettricità prodotta dai combustibili fossili (carbone, petrolio, gas),
l'elettricità prodotta col nucleare e l'elettricità prodotta con le risorse rinnovabili (idroelettrica, solare, eolica, ecc.),
focalizzandomi sul progresso avvenuto in 20 anni dal 2000 al 2020
*/
SELECT d.country, g.year_, g.electricity_from_fossil_fuels, g.electricity_from_nuclear, g.electricity_from_renewables
FROM data_2023 d, global_data g
WHERE d.country = g.country
AND (year_ = '2000' OR year_ = '2020');

/*
Quali paesi erano sul podio per produzione di energia rinnovabile?
Seleziono i 3 paesi che nel 2020 erano i maggior produttori di energia rinnovabile
*/
SELECT d.country, g.electricity_from_renewables
FROM data_2023 d, global_data g
WHERE d.country = g.country
AND g.electricity_from_renewables IS NOT NULL
AND year_ = 2020
ORDER BY g.electricity_from_renewables DESC
LIMIT 3;

/*
Quali sono i paesi che producono meno energia rinnovabile?
Seleziono i 10 paesi che nel 2020 erano i minor produttori di energia rinnovabile
*/
SELECT d.country, g.electricity_from_renewables
FROM data_2023 d, global_data g
WHERE d.country = g.country
AND g.electricity_from_renewables IS NOT NULL
AND year_ = 2020
ORDER BY g.electricity_from_renewables
LIMIT 10;

/*
In 19 anni, la produzione di energia rinnovabile e le emissioni di co2, sono aumentate?
Seleziono per ogni paese, gli anni 2000 e 2019, l'elettricità derivata dalle rinnovabili 
e le emissioni di co2 in kilotoni
*/
SELECT d.country, g.year_, g.electricity_from_renewables, g.value_co2_emissions_kt_by_country
FROM data_2023 d, global_data g
WHERE d.country = g.country
AND (year_ = '2000' OR year_ = '2019');

/*
Estraggo quanti paesi ci sono nella tabella aventi i dati aggiornati al 2020 e quali usavano l'energia nucleare nel 2020
*/
SELECT (SELECT COUNT(country) 
		FROM global_data 
		WHERE year_ = 2020) AS total_country, 
		COUNT(electricity_from_nuclear) AS total_country_with_nuclear
FROM global_data
WHERE electricity_from_nuclear > 0
AND year_ = 2020;

/*
Quali sono i paesi che iniziano per 'A'?
Seleziono i nomi dei paesi che iniziano per 'A'
*/
SELECT country
FROM data_2023
WHERE country LIKE 'A%';

/*
Quali sono i paesi che contengono una 'f'?
Seleziono i nomi dei paesi che contengono una 'f'
*/
SELECT country
FROM data_2023
WHERE country LIKE '%f%';

/*
Quali sono i paesi che finiscono per 's'?
Seleziono i nomi dei paesi che finiscono per 's'
*/
SELECT country
FROM data_2023
WHERE country LIKE '%s';

/*
Quali sono i paesi che non contengono una 'e'?
Seleziono i nomi dei paesi che non contengono una 'e'
*/
SELECT country
FROM data_2023
WHERE country NOT LIKE '%e%';

/*
Quali sono i paesi nella tabella global_data che hanno un 'H' nell'abbreviazione presa dalla tabella data_2023?
Seleziono solo i paesi da global_data eliminando i doppioni che hanno una 'H' nell'abbreviazione 
ordinandoli per ordine alfabetico decrescente
*/
SELECT DISTINCT g.country
FROM data_2023 d, global_data g
WHERE d.country = g.country
AND d.abbreviation IN (SELECT abbreviation FROM data_2023 WHERE abbreviation LIKE '%H%')
ORDER BY g.country DESC;

/*
Seleziono solo i paesi che hanno un nome con lunghezza minore o uguale a 5 caratteri
*/
SELECT country
FROM data_2023
WHERE LENGTH(country) <= 5;

/*
Seleziono i paesi e il prezzo della benzina dove la valuta monetaria è 'euro'
*/
SELECT country, gasoline_price
FROM data_2023
WHERE Currency_Code = 'EUR';

/*
Seleziono i paesi e il rispettivo linguaggio dove si parla inglese o francese
*/
SELECT country, official_language
FROM data_2023
WHERE official_language = 'English' OR official_language = 'French';

/*
Ritorna quanti paesi hanno come linguaggio ufficiale lo spagnolo
*/
SELECT COUNT(1)
FROM data_2023
WHERE official_language = 'Spanish';

/*
Ritorna quanti paesi parlano una determinata lingua
*/
SELECT official_language, COUNT(official_language) AS count_language
FROM data_2023 
GROUP BY official_language
ORDER BY count_language DESC;

/*
Ritorno tutto da "data_2023" con prefisso maggiore di 100, una popolazione minore di 30 milioni e una 'f' nel nome
*/
SELECT *
FROM data_2023
WHERE calling_code > 100
AND population < 30000000
AND country LIKE '%f%';

/*
Qual'è la seconda lingua più parlata?
Ritorna la seconda lingua più parlata tra i paesi della tabella data_2023
*/
SELECT official_language
FROM data_2023 
GROUP BY official_language
ORDER BY COUNT(official_language) DESC
LIMIT 1 OFFSET 1;

/*
Creazione di una query che ritorna country e colling_code dove calling_code ha un valore compreso tra 70 e 370
*/
SELECT country, calling_code
FROM data_2023
WHERE calling_code BETWEEN 70 AND 370;

/*
Seleziono i paesi e le corrispondenti colonne di Iscrizione lorda all'istruzione primaria e 
Iscrizione lorda all'istruzione terziaria espresse in percentuale
*/
SELECT country, gross_primary_education_enrollment, gross_tertiaryeducation_enrollment
FROM data_2023;

/*
Quali sono i paesi con la percentuale di iscrizione all'istruzione primaria lorda più alta?
Estraggo i paesi ordinandoli in base alla percentuale lorda più grande
*/
SELECT country, gross_primary_education_enrollment AS max_perc 
FROM data_2023
WHERE gross_primary_education_enrollment IS NOT NULL
ORDER BY max_perc DESC;

/*
Quali sono i paesi con la percentuale di iscrizione all'istruzione primaria lorda più bassa?
Estraggo i paesi ordinandoli in base alla percentuale lorda più piccola
*/
SELECT country, gross_primary_education_enrollment AS min_perc
FROM data_2023
WHERE gross_primary_education_enrollment IS NOT NULL
ORDER BY min_perc;

/*
Quali sono i paesi 'migliori' al livello di istruzione primaria?
Estraggo solo i paesi che hanno un' Iscrizione lorda all'istruzione primaria tra 90 e 110
ordinandoli in base alla percentuale, trovando così quali paesi sono i 'migliori' al livello di istruzione primaria
*/
SELECT country, gross_primary_education_enrollment
FROM data_2023
WHERE gross_primary_education_enrollment IS NOT NULL
AND gross_primary_education_enrollment BETWEEN 90 AND 110
ORDER BY gross_primary_education_enrollment;

/*
Quanta differenza c'è tra la popolazione complessiva e la popolazione urbana?
Creazione di una query che ritorna il paese, la popolazione, la popolazione urbana e quanta differenza c'è fra quest'ultime
*/
SELECT country, population, urban_population, (population - urban_population) AS difference,
	CASE
		WHEN (population - urban_population) > population / 2 THEN 'Maggiore del 50%'
		WHEN (population - urban_population) < population / 2 THEN 'Minore del 50%'
		ELSE 'Uguale al 50%'
	END difference_perc
FROM data_2023
WHERE population IS NOT NULL AND urban_population IS NOT NULL;

/*
Quali sono i paesi con la maggior spesa sanitaria per singolo?
Estraggo il paese e la Percentuale della spesa sanitaria totale pagata 
di tasca propria dalle persone fisiche dove il valore del dato della spesa sanitaria non è 
ordinandola per la percentuale di spesa in modo decrescente, ottenendo i paesi con la spesa maggiore 
in alto e la spesa minore in basso
*/
SELECT country, out_of_pocket_health_expenditure
FROM data_2023
WHERE  out_of_pocket_health_expenditure IS NOT NULL
ORDER by out_of_pocket_health_expenditure DESC;

/*
Estraggo il paese, la grandezza in km2, il tasso di fertilità, l'area forestale, la popolazione urbana e la popolazione
per rilevare una correlazione se c'è una correlzione tra di essi, soprattutto se il fertility rate viene influenzato 
nei paesi dove la popolazione urbana è maggiore
*/
SELECT country, agricultural_land, fertility_rate, forested_area, urban_population, population
FROM data_2023;

/*
Estraggo il paese, l'emissioni di co2 in tonnellate e l'aspettativa di vita in anni
Da questi dati possiamo vedere che l'aspettativa di vita non viene impattata direttamante dalle emissioni di co2
*/
SELECT country, co2_emissions, life_expectancy
FROM data_2023;

/*
Estraggo la percentuale di foreste e la quantità di co2 analizzare una possibile correlazione a vista
*/
SELECT forested_area, co2_emissions
FROM data_2023;

/*
Seleziono i paesi dove l'emissione di co2 in tonnellate è maggiore della metà della superficie del paese in km2
*/
SELECT country, population, land_area, co2_emissions
FROM data_2023
WHERE co2_emissions > (land_area/2);

/*
Estraggo i paesi in base a quante tonnellate di co2 producono per km2
In genere se le tonnellate di co2 per km2 superano le 1000, è considerato potenzialmente preoccupante, ma dato che non posso 
confrontare i dati ottenuti con la capacità di assorbimento naturale per km2 di ogni paese, possiamo solo dare un occhiata grezza sul problema
come possiamo notare, la differenza tra il 1° paese e il 10° è molto marcata sopratutto la punto di vista della popolazione totale,
da questa cosa possiamo dedurre che in alcuni paesi (quelli con co2 per km2), la produzione di co2 non è perfettamante suddivisa per la quantità di popolazione,
ergo significa che potrebbero esserci dei grandi sprechi (magari anche normative non rispettate) e che la co2 emessa non è una diretta conseguenza
della popolazione ma delle grandi aziende che operano in vari settori come quelli nella produzione di energia o nella produzione di vari materiali
*/
SELECT country, population, land_area AS land_area_km2, co2_emissions AS co2_emissions_in_ton, ROUND((co2_emissions / land_area),2) AS tonnellate_km2
FROM data_2023
WHERE co2_emissions IS NOT NULL
ORDER BY tonnellate_km2 DESC;

/*
Creazione di una vista 'avg_stats' (se non già esistente) con la media della percentuale di foreste e delle emissioni di co2
*/
DO $$
BEGIN
	IF NOT EXISTS (SELECT 1 FROM pg_views WHERE viewname = 'avg_stats') THEN
		EXECUTE 'CREATE VIEW avg_stats AS (
					 SELECT
						AVG(forested_area) AS avg_forest,
						AVG(co2_emissions) AS avg_co2
					 FROM 
						data_2023';
	END IF;
END$$;

/*
Creazione di una vista ‘correlation’ (se già non esistente) che ritorna il paese, l’area forestale, le emissioni di co2 e la correlazione di Pearson,
derivante da un calcolo sfuttando le colonne (co2_emissions e forested_area) prendendo solo i dati non “NULL” (non vuoti).
*/
DO $$
BEGIN
	IF NOT EXISTS (SELECT 1 FROM pg_views WHERE viewname = 'correlation') THEN
		EXECUTE 'CREATE VIEW correlation AS (
					 SELECT country, forested_area, co2_emissions, 
						ROUND((co2_emissions - AVG(co2_emissions) OVER()) / (STDDEV(co2_emissions) OVER() * 
						(forested_area - AVG(forested_area) OVER()) / (STDDEV(forested_area) OVER())), 2) AS correlation
					FROM 
						data_2023
					WHERE 
						co2_emissions IS NOT NULL OR forested_area IS NOT NULL)';
	END IF;
END$$;

/*
Elimino la vista correlation se esistente. 
(Utilizzata per cancellarla velocemente dopo le modifiche apportate alla vista per poi ricrearla)
*/
--DROP VIEW IF EXISTS correlation CASCADE;

/*
Creazione di una vista denominata “pearson” contenente i “paesi”, la “percentuale di area forestale”, le “emissioni” da
"data_2023" e “correlation” dalla precedente vista "correlation" unendola tramite la colonna “country” e aggiungendo una
colonna "Interpretazione_Pearson_correlation" che in base al valore di “correlation”, inserisce una definizione in caratteri.

(Il calcolo poteva essere contestualizzato meglio, probabilmente per un calcolo più veritiero 
avrei dovuto inserire più variabili, era principalmente per provare a mischiare più cose e allenarmi con la
sintassi)
*/
DO $$
BEGIN
	IF NOT EXISTS (SELECT 1 FROM pg_views WHERE viewname = 'pearson') THEN
		EXECUTE 'CREATE VIEW pearson AS (
					 SELECT d.country, d.forested_area, d.co2_emissions, c.correlation,
						CASE 
							WHEN c.correlation > 0.8 THEN "Forte correlazione positiva"
							WHEN c.correlation < -0.8 THEN "Forte correlazione negativa"
							ELSE "Correlazione debole o inesistente"
						END AS Interpretazione_Pearson_correlation
					 FROM 
						data_2023 d, correlation c
					 WHERE 
						d.country = c.country)';
	END IF;
END$$;

/*
Creazione di una CTE ‘conteggi’ usufruendo dei dati nella colonna "Interpretazione_Pearson_correlation" dalla precedente
vista ‘pearson’, contenente la quantità totale di righe e la quantità di righe che corrispondono ad una determinata
condizione. (Notare la necessità della mancanza delle ';' finali)
*/
WITH conteggi AS (
	SELECT
		COUNT(1) AS Totale,
		SUM(CASE WHEN interpretazione_pearson_correlation = 'Forte correlazione positiva' THEN 1 ELSE 0 END) AS Count_correlazione_positiva,
		SUM(CASE WHEN interpretazione_pearson_correlation = 'Forte correlazione negativa' THEN 1 ELSE 0 END) AS Count_correlazione_negativa,
		SUM(CASE WHEN interpretazione_pearson_correlation = 'Correlazione debole o inesistente' THEN 1 ELSE 0 END) AS Count_correlazione_debole_inesistente
	FROM pearson
)

/*
Ora sfrutto i risultati ottenuti dalla CTE “conteggi” per calcolare la suddivisione in percentuale degli elementi.
*/
SELECT
	Totale,
	ROUND(Count_correlazione_positiva * 100.0 / totale, 2) AS Count_correlazione_positiva_perc,
	ROUND(Count_correlazione_negativa * 100.0 / totale, 2) AS Count_correlazione_negativa_perc,
	ROUND(Count_correlazione_debole_inesistente * 100.0 / totale, 2) AS Count_correlazione_debole_inesistente_perc
FROM conteggi;

/*
Ritorno il paese, l'abbreviazione e il currency code, escludendo i paesi che hanno dei valori null in abbreviation o in currency code
ordinandoli per l'abbreviazione in ordine alfabetico decrescente
*/
SELECT country, abbreviation, currency_code
FROM data_2023
WHERE abbreviation IS NOT NULL AND currency_code IS NOT NULL
ORDER BY abbreviation DESC;

/*
Ritorno la popolazione totale 
*/
SELECT SUM(population) AS total_population
FROM data_2023;

/*
Ritorno il paese, la popolazione, la percentuale di lavoratori e calcolo il numero effettivo di lavoratori
*/
SELECT country, population, population_labor_force_participation, 
	CAST((population_labor_force_participation / 100) * population AS INT) AS numero_lavoratori
FROM data_2023
WHERE population_labor_force_participation IS NOT NULL;

/*
Ritorno i 3 paesi con il tasso di lavoratori più alto
*/
SELECT country, population_labor_force_participation
FROM data_2023
WHERE population_labor_force_participation IS NOT NULL
ORDER BY population_labor_force_participation DESC
LIMIT 3;

/*
Ritorno i 3 paesi con il tasso di lavoratori più basso
*/
SELECT country, population_labor_force_participation
FROM data_2023
WHERE population_labor_force_participation IS NOT NULL
ORDER BY population_labor_force_participation
LIMIT 3;

/*
Ritorno i 3 paesi per grandezza delle forze armate
*/
SELECT country, armed_forces_size AS armed_forces_size
FROM data_2023
WHERE armed_forces_size IS NOT NULL
ORDER BY armed_forces_size DESC
LIMIT 3;

/*
Calcolo la percentuale delle forze armate in base alla popolazione
*/
SELECT country, ROUND(((armed_forces_size::NUMERIC / population::NUMERIC) * 100), 6) AS armed_forces_perc
FROM data_2023
WHERE armed_forces_size IS NOT NULL;

/*
Ritorno i 10 paesi con la percentuale di forze armante più grande
*/
SELECT country, ROUND(((armed_forces_size::NUMERIC / population::NUMERIC) * 100), 6) AS armed_forces_perc
FROM data_2023
WHERE armed_forces_size IS NOT NULL
ORDER BY armed_forces_perc DESC
LIMIT 10;

/*
Ritorno il paese con la percentuale totale di tasse più basse
*/
SELECT country, total_tax_rate
FROM data_2023
WHERE total_tax_rate = (SELECT MIN(total_tax_rate)
					    FROM data_2023);

/*
Ritorno il paese, la percentuale totale di tasse e il pil, dove il pil è maggiore degli altri paesi
*/
SELECT country, gdp, total_tax_rate
FROM data_2023
WHERE gdp = (SELECT MAX(gdp)
			 FROM data_2023);

/*
Ritorno i 3 paesi con il pil più alto
*/
SELECT country, gdp
FROM data_2023
WHERE gdp IS NOT null
ORDER BY gdp DESC
LIMIT 3;

/*
Ritorno il 4°, 5° ed il 6° paese con il PIL minore della media
*/
SELECT country, gdp
FROM data_2023
WHERE gdp IS NOT null
AND gdp < (SELECT AVG(gdp) FROM data_2023)
LIMIT 3 OFFSET 3;

/*
Creo una CTE con due colonne, una con la media del Tasso di fertilità (numero medio di figli nati da una donna durante la sua vita)
e una con la media del Tasso di mortalità materna (numero di decessi materni per 100.000 nati vivi)
*/
WITH media_fertility_rate AS (
	SELECT AVG(fertility_rate) AS media_fertility_rate
	FROM data_2023),
	
	media_maternal_mortality_ratio AS (
	SELECT AVG(maternal_mortality_ratio) AS media_maternal_mortality_ratio
	FROM data_2023)

-- Controllo il contenuto delle seguenti CTE
SELECT *
FROM media_fertility_rate, media_maternal_mortality_ratio;

/*
Estraggo i paesi in base al Tasso di fertilità (numero medio di figli nati da una donna durante la sua vita) più basso e 
il birth_rate (Numero di nascite per 1.000 abitanti all'anno), come ci aspettavamo, all'aumentare della fertilità, c'è un aumento
delle nascite, salvo alcune eccezioni dove pur avendo una fertilità bassa, il tasso di natalità è comunque buono
*/
SELECT country, fertility_rate, birth_rate
FROM data_2023
WHERE fertility_rate IS NOT NULL
ORDER BY fertility_rate;

/*
Estraggo i paesi in base al Tasso di mortalità materna (numero di decessi materni per 100.000 nati vivi) più alto
*/
SELECT country, maternal_mortality_ratio
FROM data_2023
WHERE maternal_mortality_ratio IS NOT NULL
ORDER BY maternal_mortality_ratio DESC;

-- Se già esistente elimino la tabella temporanea "copia_data_2023"
DROP TABLE IF EXISTS copia_data_2023;

/*
Creazione di una tabella temporanea "copia_data_2023" (se non esistente) che fa da copia della tabela data_2023.
In genere questa azione viene usata per fare dei test sulle colonne della tabella senza coinvolgere la tabella principale,
da utilizzare soprattutto per testare operazioni di modifica o di eliminazione,
per poi successivamente effettuarle su quest'ultima per evitare che qualche svista nelle query, come ad esempio "UPDATE copia_data_2023 SET gasoline_price = 1.71"
senza un "WHERE", ci possa far fare danni quasi irreparabili
*/
CREATE TEMP TABLE copia_data_2023 AS (
		SELECT *
		FROM data_2023
);

/*
Inoltre prima di effettuare una modifica è consigliabile usare la query BEGIN TRANSACTION O START TRANSACTION
così da avere la possibilità di annullare o confermare le modifiche
*/
BEGIN TRANSACTION;
START TRANSACTION;

-- Controllo se c'è qualche valore null, tipo il prezzo della benzina
SELECT *
FROM copia_data_2023
WHERE country = 'San Marino';

-- Possiamo modificare un valore di una colonna
UPDATE copia_data_2023 SET gasoline_price = 1.71 WHERE country = 'San Marino';

-- Possiamo inserire una nuova riga
INSERT INTO copia_data_2023 (country, population) VALUES ('Springfield', 30720);

-- Controllo che l'inserimento sia andato a buon fine
SELECT *
FROM copia_data_2023
WHERE country = 'Springfield';

-- Possiamo eliminare una riga
DELETE FROM copia_data_2023 WHERE country = 'Springfield';

-- Controllo che l'eliminazione sia andata buon fine (potrei riusare la query sopra senza riscriverla)
SELECT *
FROM copia_data_2023
WHERE country = 'Springfield';

-- Se siamo soddisfatti delle modifiche, confermiamo la transazione con commit
COMMIT;

-- Se vogliamo annullare le modifiche, usiamo rollback
ROLLBACK;

-- Se già esistente elimino la tabella temporanea "prova"
DROP TABLE IF EXISTS prova;

/*
Creazione di una tabella temporanea "prova" (se non già esistente) con quattro colonne (era stata creata per ospitare il risultato sottostante, ma preferisco la soluzione successiva)
*/
CREATE TEMP TABLE prova(
			country1 VARCHAR(255),
			inf_mort_from_min NUMERIC,
			country2 VARCHAR(255),
			inf_mort_from_max NUMERIC
);

/*
Creazione di una query di 5 parti, due con il paese e la mortalità infantile ordinate dal valore più basso al valore
più alto, due con il paese e la mortalità infantile ordinate dal valore più alto al valore più basso, e una con la
differenza di punti percentuali, così da avere subito un confronto a specchio sulla differenza del tasso di mortalità
fra i primi e gli ultimi valori.
Ad esempio, si può anche osservare la differenza che c'è tra il 1° e il 10° paese con il tasso di mortalità più basso, 
è abbastanza trascurabile (0.8 punti percentuale, quindi con un margine di miglioramento minimo),
mentre la differenza tra i 1° e il 10° paese con il tasso di mortalità più alto,
è molto rilevante (21.9 punti percentuale, quindi con un margine di miglioramento molto alto)
*/
SELECT 
	q1.country, q1.infant_mortality AS infant_mortality_min_to_max , q2.country, q2.infant_mortality AS infant_mortality_max_to_min,
	-(q1.infant_mortality - q2.infant_mortality) AS differenza_punti_percentuale
FROM 
	(SELECT country, infant_mortality, ROW_NUMBER() OVER(ORDER BY infant_mortality) AS rn
	 FROM data_2023
	 WHERE country IS NOT NULL AND infant_mortality IS NOT NULL) AS q1  
JOIN
	(SELECT country, infant_mortality, ROW_NUMBER() OVER(ORDER BY infant_mortality DESC) AS rn
	 FROM data_2023
	 WHERE country IS NOT NULL AND infant_mortality IS NOT NULL ) AS q2
ON 
	q1.rn = q2.rn;









