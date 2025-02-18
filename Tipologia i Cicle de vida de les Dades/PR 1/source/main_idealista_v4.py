import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pandas as pd
import re


def init_driver():
    """Inicialitza el driver de Chrome amb opcions per evitar deteccions i maximitza la finestra.
    - Desactiva característiques del motor Blink
    - Mode incògnit
    - Desactivar sandbox per evitar errors de permisos
    - Canvi del agent del navegador a un específic
    """
    options = uc.ChromeOptions()
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--incognito")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument(
        "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)"
    )

    driver = uc.Chrome(options=options)
    driver.maximize_window()
    return driver


def navigate_to_website(driver, url):
    """Accedeix al lloc web i accepta les cookies"""
    driver.get(url)
    try:
        accept_cookies_button = WebDriverWait(driver, 15).until(
            EC.element_to_be_clickable(
                (By.XPATH, "//button[@id='didomi-notice-agree-button']")
            )
        )
        accept_cookies_button.click()
    except TimeoutException:
        print("Botó d'acceptar cookies no trobat o no clickable.")


def scrape_page(driver):
    """Extrau les dades d'una pàgina de Idealista i retorna una llista de diccionaris amb les dades"""
    WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".item-info-container"))
    )

    height = driver.execute_script("return document.body.scrollHeight")
    for e in range(0, height, 700):
        driver.execute_script(f"window.scrollTo(0, {e});")
        time.sleep(2)

    time.sleep(3)

    listings = driver.find_elements(By.CSS_SELECTOR, ".item-info-container")
    data_list = []

    for listing in listings:
        data = {
            # Busca l'element ".item-price" dins de "listing"
            "preu_actual": listing.find_element(By.CSS_SELECTOR, ".item-price")
            .text.replace("\n", "")
            .strip()
            if listing.find_elements(By.CSS_SELECTOR, ".item-price")
            else "",
            # Busca l'element ".pricedown_price"
            "preu_original": listing.find_element(
                By.CSS_SELECTOR, ".pricedown_price"
            ).text.strip()
            if listing.find_elements(By.CSS_SELECTOR, ".pricedown_price")
            else "",
            # Busca l'element ".pricedown_icon", si no es troba es posa 0% per defecte
            "descompte": listing.find_element(
                By.CSS_SELECTOR, ".pricedown_icon"
            ).text.strip()
            if listing.find_elements(By.CSS_SELECTOR, ".pricedown_icon")
            else "0%",
            # Busca l'element ".item-link" i recull el text, també es recull "href" per enllaç
            "titol": listing.find_element(By.CSS_SELECTOR, ".item-link").text.strip()
            if listing.find_elements(By.CSS_SELECTOR, ".item-link")
            else "",
            "enllaç": listing.find_element(By.CSS_SELECTOR, ".item-link").get_attribute(
                "href"
            )
            if listing.find_elements(By.CSS_SELECTOR, ".item-link")
            else "",
            # Busca l'element ".item-description p.ellipsis"
            "descripcio": listing.find_element(
                By.CSS_SELECTOR, ".item-description p.ellipsis"
            ).text.strip()
            if listing.find_elements(By.CSS_SELECTOR, ".item-description p.ellipsis")
            else "",
            # Busca l'element ".hightop-agent-name", si no es troba es posa "Particular"
            "agent_nom": listing.find_element(
                By.CSS_SELECTOR, ".hightop-agent-name"
            ).text.strip()
            if listing.find_elements(By.CSS_SELECTOR, ".hightop-agent-name")
            else "Particular",
            # Busca l'element ".item-parking", si no es troba es posa "No indicat"
            "parking": listing.find_element(
                By.CSS_SELECTOR, ".item-parking"
            ).text.strip()
            if listing.find_elements(By.CSS_SELECTOR, ".item-parking")
            else "No indicat",
            # Busca l'element ".listing-tags" i es crea una llista separant per comes
            "tags": ", ".join(
                [
                    tag.text.strip()
                    for tag in listing.find_elements(By.CSS_SELECTOR, ".listing-tags")
                ]
            ),
        }

        # Es fan servir expressions regulars per extreure els dormitoris i metres quadrats
        detail_elements = listing.find_elements(By.CSS_SELECTOR, ".item-detail")
        for detail_element in detail_elements:
            detail_text = detail_element.text.strip()
            if "dorm." in detail_text:
                habs_match = re.search(r"(\d+)\s*dorm.", detail_text)
                data["habs"] = habs_match.group(1) if habs_match else ""
            elif "m²" in detail_text:
                metres_match = re.search(r"(\d+)\s*m²", detail_text)
                data["metres2"] = metres_match.group(1) if metres_match else ""

        data_list.append(data)
    return data_list


def save_data(data_list, file_name):
    """Guarda els elements en format .csv"""
    data = pd.DataFrame(data_list)
    data.to_csv(f"{file_name}.csv", index=False)


def main():
    driver = init_driver()
    website = "https://www.idealista.com/ca/venta-viviendas/barcelona-barcelona/"
    navigate_to_website(driver, website)
    all_data = []

    for page in range(1, 11):
        data = scrape_page(driver)
        all_data.extend(data)
        if page < 10:
            next_page = f"https://www.idealista.com/ca/venta-viviendas/barcelona-barcelona/pagina-{page + 1}.htm"
            driver.get(next_page)
            WebDriverWait(driver, 30).until(
                EC.presence_of_all_elements_located(
                    (By.CSS_SELECTOR, ".item-info-container")
                )
            )
            time.sleep(5)

    save_data(all_data, "idealista_dades_exteses")
    driver.quit()


if __name__ == "__main__":
    main()
