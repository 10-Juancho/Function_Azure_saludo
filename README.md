# Ejecucion local (Azure Fuctions)
####  1. Clonar el repositorio.

git clone https://github.com/10-Juancho/Function_Azure_saludo.git
#### 2. Entrar a la carpeta.
cd tu-proyecto

####  3. Crear el entorno virtual.
``` Terminal
python -m venv venv
```

#### 4. Activarlo
**Windows:**

> venv\Scripts\activate

**Mac/Linux:**

> source venv/bin/activate

### 5. Instalar dependencias

> pip install -r requirements.txt

### 6. Instalar herramientas de Azure Functions
> pip install azure-functions

###  7. Iniciar la función
> func start


# ☁️ API YA DESPLEGADA.

https://saludar.azurewebsites.net/api/http_saludar

Ej: consumir la API 

> https://saludar.azurewebsites.net/api/http_saludar?nombre=juan





# 👋 Azure Function – Saludar

Este proyecto implementa una **función serverless en Azure Functions**, desarrollada en **Python**, que responde un saludo personalizado cuando el usuario envía un nombre como parámetro de consulta en una petición HTTP.


## 🚀 Características

- Programada con **Python y Azure Functions**
- Desplegada en **Azure Functions App**
- Invocable mediante **HTTP (API REST)**
- No requiere token (nivel de seguridad: `Anonymous`)
- Responde con un saludo usando el nombre recibido


---
### 📂 Estructura del Proyecto

├── function_app.py<br>
├── requirements.txt<br>
└── host.json


## 🧠 Código de la Función
```Python
import azure.functions as func
import logging

# Se crea una aplicación de Azure Functions con nivel de autenticación anónimo,
# lo que significa que cualquier usuario puede invocar esta función sin autenticarse.
app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

# Se define una función accesible por HTTP con la ruta "http_saludar"
@app.route(route="http_saludar")
def http_saludar(req: func.HttpRequest) -> func.HttpResponse:
    # Se registra en el log que la función fue invocada
    logging.info('Python HTTP trigger function processed a request.')

    # Se intenta obtener el parámetro "nombre" enviado en la URL (cadena de consulta)
    name = req.params.get('nombre')

    # Si no viene el nombre en la URL, se intenta recuperarlo desde el cuerpo de la petición
    if not name:
        try:
            # Se intenta leer el cuerpo como JSON
            req_body = req.get_json()
        except ValueError:
            # Si no se puede leer como JSON, se ignora el error
            pass
        else:
            # Si el JSON es válido, se busca el campo "nombre"
            name = req_body.get('nombre')

    # Si se recibió el nombre correctamente
    if name:
        # Se responde con un mensaje personalizado
        return func.HttpResponse(
            f"Hello, {name}. This HTTP triggered function executed successfully."
        )
    else:
        # Si no se envió ningún nombre, se devuelve mensaje genérico
        return func.HttpResponse(
             "Esta función activada por HTTP se ejecutó correctamente. "
             "Pasa un nombre en la cadena de consulta o en el cuerpo de la petición para obtener una respuesta personalizada.",
             status_code=200
        )

```
## 🔍 Resumen de lo que hace la función:

- La función se activa mediante una llamada HTTP.

- Intenta obtener el parámetro "nombre" ya sea:

    - desde la URL (ej: ...?nombre=Juan)

    - o desde el cuerpo JSON de la petición.

- Si lo encuentra, devuelve un saludo personalizado.

- Si no, responde con un mensaje genérico indicando cómo enviar un nombre.