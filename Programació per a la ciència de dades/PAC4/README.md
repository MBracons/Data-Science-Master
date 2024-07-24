# README: PAC 4 - Programació per a la ciència de dades

## Descripció

Aquest projecte en Python està dissenyat per a descomprimir i llegir dades sobre sèries de televisió en format CSV
i posteriorment processar, filtrar i visualitzar-les. El fitxer principal main.py està format de diverses funcions
modulars agrupades en funció de la seva finalitat.

## Mòduls i funcions 

El fitxer principal *main.py* utilitza els següents mòduls i funcions:
- DescompressioLectura: Conté les funcions per descomprimir arxius i llegir dades a DataFrames o diccionaris.
  - Mòdul *descomprimir.py*: Conté la funció **descomprimir**, descomprimeix un fitxer (amb format .zip o .tar.gz) 
  situat en una ruta especificada i extreu el seu contingut en una ruta de destinació també especificada.
  - Mòdul *llegir.py*: Conté les funcions **llegir_to_df** i **llegir_to_dict** llegeixen i combinen tots els arxius CSV 
  dins d'un directori especificat, creant respectivament un DataFrame de pandas i un diccionari en Python, utilitzant 
  la columna 'id' com a clau principal per a la fusió.

- Processament: Conté les funcions per a modificar els DataFrames.
  - Mòdul *afegir_variable.py*: Conté la funció **afegir_variable** que calcula i afegeix una nova columna anomenada
  'air_days' a un DataFrame, representant el nombre total de dies que una sèrie de televisió ha estat en
  emissió, basant-se en les dates d'inici i finalització de la sèrie.
  - Mòdul *crear_diccionari.py*: Conté la funció **crear_diccionari** que genera un diccionari a partir d'un DataFrame, 
  on cada clau correspon al nom original d'una sèrie de televisió, i el seu valor associat és una URL formada per la 
  concatenació dels camps 'homepage' i 'poster_path' de la sèrie. Si algun d'aquests camps és invàlid o inexistent,
  el valor del diccionari serà 'NOT AVAILABLE'.

- Filtratge: Conté les funcions per a filtrar un DataFrame segons diferents criteris.
  - Mòdul *filtrar.py*: Conté diverses funcions de filtratge
    - **filtrat_idioma_resum**: Filtra les sèries que estan en anglès ('en') i tenen les paraules 'mystery' o 
    'crime' en el seu resum.
    - **filtrat_any_cancellada**: Selecciona les sèries que van començar en un any específic i han estat cancel·lades.
    - **filtrat_any**: Filtra les sèries que van començar en un any específic, sense considerar el seu estat actual.
    - **filtrar_idioma**: Filtra les sèries basant-se en un idioma específic, tant en la columna 'original_language'
    com en 'languages'.
    - **filtra_df_en_parallel**: Aplica una funció de filtratge donada a un DataFrame utilitzant múltiples fils
    (threads) per accelerar el procés, útil per treballar amb grans conjunts de dades.
    
- Visualització: Conté les funciones per a mostrar gràficament les dades.
  - Mòdul *grafics.py*: Conté les funcions que generen gràfics per analitzar les dades de sèries de 
  televisió en un DataFrame.
    - **grafic_any**: Crea un gràfic de barres que mostra la distribució del nombre de sèries de televisió segons l'any
    en què van començar, utilitzant la columna 'first_air_date'.
    - **grafic_type**: Genera un gràfic de línies que representa el nombre de sèries de cada categoria 
    (definida en la columna "type") produïdes en cada dècada, començant des d'un any inicial especificat.
    - **grafic_genres**: Crea un gràfic circular que il·lustra el percentatge de sèries per gènere, 
    agrupant els gèneres menys comuns sota la categoria "Altres" i etiquetant només aquells segments 
    que representen més d'un 5% del total.
  
- utils: Conté les funcions que s'utilitzen com a eina durant el projecte
  - Mòdul *mesura_temps.py*: Conté la funció **mesura_temps** que mesura i imprimeix el temps mínim de processament d'una
  funció específica, realitzant aquesta mesura a través de dues repeticions i tres execucions per repetició. 
  Això permet obtenir una estimació més precisa del temps de processament en diferents condicions d'execució.

## Execució del Programa

El programa *main.py* es pot executar amb diferents arguments per executar els exercicis per separat o tots de cop.
- 'python main.py' al terminal per executar tots els exercicis en ordre.
- 'python main.py n' per executar l'exercici n-èssim.
  - Com els exercicis per n>1 requereixen el DataFrame, a *main.py* hi ha la funció *exercici_aux* que s'executa quan 
  n>1 per generar el DataFrame de l'exercici 1 sense les parts innecessàries per a la resta d'exercicis.
  -  *exercici_aux* genera el DataFrame a partir de les dades, però han hagut de ser descomprimides almenys un cop
     (executant l'exercici 1).
- En l'exercici 4 es mostren gràfiques, l'usuari ha de tancar manualment la figura per a que el codi segueixi executant
  línies de codi.

## Tests Unitaris

A cada una de les carpetes dels mòduls de les funcions hi ha també les funcions de test, que tenen el prefix *test_*.
Aquestes es poden executar al terminal fent 'python test_{nom}'.
També és possible utilitzar *coverage* per veure la cobertura dels test, tot i això en el fitxer *coverage.txt* ja hi
ha els resultats obtinguts.
  - Per reproduïr els test de cobertura: 'coverage run {nom_del_test}' i 'coverage report' al terminal.

### Funcionament 

- *test_descomprimir*: Es vol avaluar la funcionalitat del mètode de descompressió de fitxers.
  - Es crea un directori per a fer els test.
  - Es creen dos fitxers CSV.
  - Es comprimeixen.
  - Es fa servir el mètode de descompressió.
  - Es mira si hi ha els mateixos CSV.
  - Es neteja el directori on s'han fet els test.

- *test_llegir.py*: Es volen avaluar els mètodes de lectura CSV a DataFrame  i a Diccionari
  - Es crea un directori temporal
  - Es generen dos CSV
  - Es defineix la funció *crear_csv_prova* que omple els CSV amb contingut conegut
  - Es fan servir els mètodes 'llegir_to_df' i 'llegir_to_dict' i es mira si el nombre de columnes/entrades és l'esperat
  - Es neteja el directori

- *test_filtrar.py*: Es vol mirar si les funcions de filtratge funcionen correctament

  - Filtrar idioma i resum, combinacions: idioma correcte i les dues paraules correctes; 
  idioma correcte i una primera paraula correcta; idioma correcte i segona paraula correcta; idioma 
  correcte i paraules incorrectes; idioma incorrecte i primera paraula correcta; idioma incorrecte 
  i segona paraula correcta; idioma incorrecte i les dues paraules correctes;
  idioma incorrectes i les dures paraules incorrectes.
    - es genera un dataFrame amb totes les combinacions possibles per a obtindre els resultats de la funció 'filtrar_idioma_resum'
    - de tots els resultats possibles n'haurien de quedar 3.
      
  - Filtrar any i cancel·lada, combinacions: 4 variacions de anys correctes/incorrectes i estats cancel·lats/altres.
    - Es fa servir el mètode 'filtrat_any_cancellada'
    - Es mira si hi ha 1 resultat
  
  - Filtrat idioma, combinacions: Fan combinacions correctes/incorrectes de 'original_language' i 'languages'
    - Es mira si hi ha 2 registres
    - Un que té idioma correcte en 'original_language'
    - Un que té idioma correcte en 'languages'
  
- *test_afegir_variable.py*: Es vol mirar si s'afegeix la variable correctament
  - Es crea un dataframe amb una entrada que te 'name', 'first_air_date' i 'last_air_date' coneguts.
  - Es mira si la variable afegida existeix i té el resultat esperat

- *test_crear_diccionari*: Es vol mirar si es guarden els posters correctes al diccionari
  - Es creen tres combinacions de 'name', 'homepage' i 'poster_path'
  - Es mira si es dona la direcció correcta o 'NOT AVAILABLE' quan toca.
