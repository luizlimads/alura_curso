from extratorUrl import ExtratorURL

verifica_url = 'bytebank.com/cambio \
bytebank.com.br/cambio \
www.bytebank.com/cambio \
www.bytebank.com.br/cambio \
http://www.bytebank.com/cambio \
http://www.bytebank.com.br/cambio \
https://www.bytebank.com/cambio \
https://www.bytebank.com.br/cambio \
https://bytebank/cambio \
http://bytebank.naoexiste/cambio \
ht:bytebank.naoexiste/cambio'.split()

lista_url = []
for x in verifica_url:
    try:
        lista_url.append(ExtratorURL(x))
    except:
        pass

print(len(lista_url))