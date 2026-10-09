# Pre-entrega: Automatización de SauceDemo

## Propósito del proyecto

Este proyecto automatiza pruebas funcionales básicas sobre la aplicación demo de SauceDemo para validar flujos de login, catálogo y carrito de compras usando Selenium WebDriver y Pytest.

## Tecnologías utilizadas

- Python 3
- Pytest
- Selenium WebDriver
- ChromeDriver
- HTML report generado por pytest-html

## Estructura del proyecto

- `tests/`: archivos de pruebas automatizadas
- `utils/`: funciones auxiliares reutilizables
- `reports/`: reportes HTML generados por pytest

## Instalación de dependencias

1. Crear un entorno virtual:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. Instalar dependencias:

   ```bash
   pip install pytest selenium pytest-html
   ```

3. Verificar que Chrome y ChromeDriver estén instalados en el sistema.

## Ejecución de pruebas

Para ejecutar la suite completa:

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

Para ejecutar un caso puntual:

```bash
pytest tests/test_login.py -v
```

## Casos cubiertos

- Login exitoso con credenciales válidas
- Verificación del catálogo de productos
- Validación de título, menú y filtros
- Agregado de un producto al carrito
- Verificación del contador del carrito y contenido del carrito

## Observaciones

Las pruebas están diseñadas para ejecutarse de forma independiente, cerrando el navegador en cada caso con `finally` para evitar fugas de recursos.
