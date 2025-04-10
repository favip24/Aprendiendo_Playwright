# Importamos el tipo Page de Playwright
# Permite autocompletado, mejor lectura y trabajr de forma explícita con una instancia de página

from playwright.sync_api import Page  # Representa una pestaña del navegador
import pytest  # Imprtamos Pytest, ejecuta los test (funciones terminadas con 'test_')

# Primer Test: Verifica el Título
def test_title(page: Page):  # Función que te da una página ya lista para usar
    page.goto("/")  # Va a la URL raíz (en consola por ejemplo la URL base es https://www.saucedemo.com)
    print("Título actual:", page.title())  # Prints para Debug
    assert page.title() == "Swag Labs"  # Verifica que el título de la página sea "Swag Lab". Caso contrario el test falla
    page.screenshot(path="screenshots/title_ok.png")  # Captura en caso de éxito (evidencia)


# Segundo Test: Validar Restricción Sin Login
def test_inventory_page(page: Page):
    page.goto("/inventory.html")  # Accede directamente a la página dle inventario, que en esta app requiere login
    assert page.is_visible("h3")  # Verifica que el elemento existe antes de leer su texto
    error_msg = page.inner_text("h3")
    print("Mensaje Recibido:", error_msg)
    assert error_msg == "Epic sadface: You can only access '/inventory.html' when you are logged in."
    # Busca el texto dentro de la etiqueta 'h3', y verifica que sea el mensaje de error esperable
    page.screenshot(path="screenshots/inventory_error.png")  # Captura

# Iniciar Test: pytest --base-url https://www.saucedemo.com
# Iniciar Test con Navegador Específico: pytest --base-url https://www.saucedemo.com --browser firefox
# [URL TEST](http://www.saucedemo.com)