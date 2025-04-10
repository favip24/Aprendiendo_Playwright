import asyncio  # Maneja código asíncrono en Python
from playwright.async_api import async_playwright


async def main():  # Función asíncrona, por dentro usamos 'await'
    async with async_playwright() as p:  # Usamos PW asíncrono sin bloqueos
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.goto("http://whatsmyuseragent.org/")
        print(await page.title())
        await browser.close()

asyncio.run(main())

# 'async def': define una función asíncrona
# 'await': hace que el programa espere a que termine una tarea antes de seguir
# Sin el 'await', el código sigue sin esperar respuestas causando errores
