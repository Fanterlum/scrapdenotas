Universidad de Guadalajara
Computación Tolerante a fallas

González García Vicente 217538047

Flore Martínez Hermes Gabriel 217548433


# **Journal E-bot**
Este proyecto tiene como objetivo extraer noticias relacionadas con tecnología de diferentes sitios web y realizar tareas como el parafraseo de los textos y guardar la información en un documento de Word.

## Librerías Utilizadas
El código utiliza las siguientes librerías:

time: para gestionar pausas y esperas en el código.
docx: para trabajar con documentos de Word.
os: para interactuar con el sistema operativo y gestionar archivos.
keyboard: para simular acciones de teclado.
selenium.webdriver: para automatizar la navegación web.
prefect: para la definición y ejecución de flujos de tareas.
newspaper: para extraer artículos de noticias de diferentes sitios web.
docx.shared: para trabajar con estilos y formatos en los documentos de Word.
selenium.webdriver.common.action_chains: para realizar acciones de teclado y mouse en Selenium.
## Variables de URL
El código utiliza las siguientes variables para almacenar las direcciones URL de los sitios web que se utilizarán:

url_parafrasis: URL del sitio web para parafrasear textos.
url_Milenio: URL del sitio web Milenio que contiene noticias de tecnología.
url_ElUniversal: URL del sitio web El Universal que contiene noticias de tecnología.
url_ElEconomista: URL del sitio web El Economista que contiene noticias de tecnología.
url_Gaceta: URL del sitio web Gaceta de la Universidad de Guadalajara.
## Listas de URLs y Notas
El código utiliza las siguientes listas para almacenar los URLs de las noticias y las notas extraídas:

urls: lista para almacenar todos los URLs de las noticias.
nota: lista para almacenar el título, texto y URL de cada nota.
urls_usados: lista para almacenar los URLs de las noticias que han sido utilizados.
## Funciones de Extracción y Parafraseo
El código utiliza las siguientes funciones para extraer el texto de los artículos y parafrasearlos:

extraerTextoArticulo(url): función para extraer el título y el texto de un artículo a partir de su URL. Si el artículo no cumple con los requisitos de longitud, se descarta.
traerLosLinks(): función para obtener los URLs de las noticias de tecnología de los sitios web especificados.
parafrasearLink(texto): función para parafrasear el texto utilizando el sitio web indicado.
Funciones de Escritura en Documento
El código utiliza las siguientes funciones para escribir y guardar las notas en un documento de Word:

writeonDoc(): función para escribir la nota en el documento de Word especificado.
imprimirLinksUsados(): función para imprimir los URLs de las noticias utilizadas.
## Flujo del Proceso
El código define el flujo del proceso utilizando la librería prefect. El flujo se compone de las siguientes tareas:

traerLosLinks(): obtiene los URLs de las noticias de tecnología.
extraerTextoArticulo(url): extrae el texto de cada artículo y realiza filtrado.
parafrasearLink(texto): parafrasea el texto del artículo.
writeonDoc(): escribe y guarda la nota en el documento de Word.
imprimirLinksUsados(): imprime los URLs de las noticias utilizadas.
El flujo se ejecuta llamando a la función proceso().

¡Eso es todo! Este es un resumen de las secciones principales del código y cómo funciona
