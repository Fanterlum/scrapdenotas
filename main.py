from newspaper import Article

url = 'https://www.milenio.com/tecnologia/gadgets/sony-lanza-inzone-marca-productos-gamers'
def extraerTextoArticulo(url):

    mi_Articulo = Article(url, language="es")
    mi_Articulo.download()
    # print(mi_Articulo.html)
    mi_Articulo.parse()
    # extarer articulo
    print('titulo: ', mi_Articulo.title)
    print('articulo: ', mi_Articulo.text)

extraerTextoArticulo(url)