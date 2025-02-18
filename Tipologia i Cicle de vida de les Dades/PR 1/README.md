# README

Repositori per a la pràctica 1 de l'assignatura de Tipologia i Cicle de vida de les Dades del Màster universitari de Ciència de Dades de la UOC

## Alumnes:
- Marc Bracons
- Ariadna Bosch

## Descripció:
Aquest script Python utilitza la biblioteca undetected_chromedriver per iniciar una sessió automatitzada de Chrome amb opcions específiques per evitar deteccions. L'objectiu principal és recollir dades de llistats de propietats del lloc web Idealista i guardar aquestes dades en format CSV.

## Dependencies:
- Python 3.x
- pandas
- selenium
- undetected_chromedriver
- re (expressions regulars)

## Instal·lació:
Instal·la els paquets necessaris amb pip:
$ pip install -r requirements.txt

Estructura del codi:
1. `init_driver`: Inicialitza el driver de Chrome amb opcions específiques.
2. `navigate_to_website`: Accedeix al lloc web i gestiona les cookies.
3. `scrape_page`: Recull dades dels llistats de propietats de la pàgina actual.
4. `save_data`: Guarda les dades recollides en fitxers CSV.
5. `main`: Funció principal que executa les funcions anteriors en l'ordre especificat.

## Ús:
Executa el script des del terminal:
$ python main_idealista_v4.py

Aquest script recollirà dades de les primeres 10 pàgines dels llistats de propietats a Barcelona i guardarà els resultats en un fitxer anomenat 'idealista_dades_exteses.csv'.

Nota:
El script ha estat configurat per treballar amb el lloc web en la seva estructura actual. Canvis en el lloc web poden requerir ajustaments al codi.
