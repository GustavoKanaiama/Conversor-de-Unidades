# Conversor-de-Unidades
Aplicativo conversor de unidades usando Python+GTK

## Configurando o aplicativo
É possível configurar o arrquivo "config.txt" que se encontra mesma pasta de execução do arquivo '.py' do apliccativo.

### Inserindo/Removendo unidades
As medidas seguem um formato específico no arquivo. 

Exemplo:
```
<Nome-da-unidade1>
<Unidade de Referência> - 1
<Outra unidade1> - <valor em rerlação ao de referência>
<Outra unidade2> - <valor em rerlação ao de referência>
<Outra unidade3> - <valor em rerlação ao de referência>
# <separador, indicando o final da unidade>
<Nome-da-unidade2>
<Unidade de Referência> - 1
<Outra unidade4> - <valor em rerlação ao de referência>
```

Exemplo real aplicado:
```
Volume
Litro - 1
Mililitro - 1000
Galao americano - 0.264172
#
Pressao
Bar - 1
Torr - 750.062
```
Neste exemplo há duas unidades ("Volume" e "Pressao") cada uma delas com seu valor de rerferência. "1 bar equivalem a 750.062 Torr". Por fim, é necessário utilizar o ponto '.' como separador decimal.