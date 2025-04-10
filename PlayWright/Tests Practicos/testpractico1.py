# Ejercicio: Automatizar una búsqueda en Google y capturar el resultado #
# Objetivo:
# Abrir el navegador con Playwright.
# Ir a Google.
# Escribir un término en la barra de búsqueda.
# Presionar "Enter" para buscar.
# Capturar el primer resultado y mostrarlo en consola.
# Tomar una captura de pantalla. #
from playwright.sync_api import sync_playwright


def google_search():  # Define la función en Python
    with sync_playwright() as p:  # Inicia y gestiona automáticamente PlyWrght
        # Se abre el navegador
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Se dirige a la URL (Google)
        page.goto("https://www.google.com")

        # Busca la barra de búsqueda
        search_box = page.locator("textarea[name='q']")  # Selecciona le input
        search_box.fill("Automatización con Playwright")
        search_box.press("Enter")  # Realiza la búsqueda

        # Esperar a que cargue los datos
        page.wait_for_selector("h3")

        # Obtener el primer resultado
        fist_result = page.locator("h3").first.text_content()
        print(f"Primer resultado: {fist_result}")  # Imprime en consola

        # Captura de pantalla
        page.screenshot(path="google_search.png")

        # Cierra el navegador
        browser.close()


google_search()
