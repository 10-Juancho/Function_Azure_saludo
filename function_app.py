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