from playwright.sync_api import sync_playwright
# Importamos la API síncrona de Playwright
# Nos permite automatizar el navegador de forma secuencial (paso a paso)

with sync_playwright() as p:  # Inicia Playwright
    browser = p.chromium.launch(headless=False)  # Navegador interfaz visible
    page = browser.new_page()  # Creamos nueva página
    page.goto("http://whatsmyuseragent.org/")  # Cargamos la URL
    page.screenshot(path="demo.png")  # Tomamos una captura de pantalla
    browser.close()  # Cerramos el navegador

# 'with': Cuando el bloque de código termina, se cierra automáticamente
#  python 'synbc.py' para ejecutar el test
