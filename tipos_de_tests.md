# TIPOS DE TESTS AUTOMATIZADOS #

*Test de Navegación*
- Verificar que se pueda acceder a una URL.
- Asegurar que redirecciones funcionen.
- Comprobar que los enlaces lleven al lugar correcto.

*Test de Login (Positivo y Negativo)*
- Ingresar credenciales correctas ➝ acceder al sistema.
- Ingresar datos inválidos ➝ mostrar mensaje de error.

*Test de Formularios*
- Completar inputs (textos, selects, checkboxes, radios).
- Validar mensajes de éxito o error tras enviar el formulario.

*Test de Componentes*
- Validar que un botón esté habilitado/deshabilitado.
- Verificar comportamiento de un modal o dropdown.

*Test Visual o de Layout*
- Capturar screenshots y compararlas si hicieras regresión visual.
- Verificar si los elementos aparecen en su lugar o en determinado orden.

*Test de Red (Network Requests)*
- Escuchar llamadas HTTP (API).
- Validar que respondan correctamente (200, 404, etc.).

*Sitios Web a Probar*
1. SauceDemo
Ideal para login, validaciones y navegación entre productos.

2. The Internet - Herokuapp
Gran variedad de prácticas: checkboxes, drag & drop, formularios, alerts, etc.

3. Automation Practice
E-commerce completo: login, registro, productos, carrito, pago, etc.

4. Reqres.in
API de prueba para practicar tests automatizados sobre servicios REST.

5. Playwright.dev Testing Playground
Tienen ejemplos para testear botones, inputs y otras interacciones.

*Frameworks*
Es una estructura organizada que te permite:

- Separar responsabilidades:
    + Tests por un lado.
    + Configuraciones por otro.
    + Utilidades comunes en otro archivo.

- Escalar sin volverte loco:
    + Agregar nuevos tests sin repetir código.

- Ejecutar con facilidad:
    + Desde consola, con un solo comando.
    
- Obtener reportes automáticos.