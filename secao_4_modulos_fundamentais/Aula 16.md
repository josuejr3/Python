
#### <span style="color:rgb(4, 255, 0)">JSON</span>

JSON (Javascript Object Notation) é uma estrutura de dados que permite a serialização de objetos em texto simples que permite facilitar a transmissão de dados através da rede, APIs web ou outros meios de comunicação. 

O JSON suporta os seguintes tipos de dados: 

-  Números: podem ser tanto inteiros como com ponto flutuante, ex: 43 e 3.14;
-  Strings: são cadeias de caracteres, como "Hello World!" ou "12345";
	-  Obs: as strings devem ser envolvidas por aspas duplas.
-  Booleanos: são os valores verdadeiro (true) ou falso (false);
-  Arrays: são listas ordenadas de valores, ex: [1, 2, 3] ou ["Oi", "Ola", "Bom dia"];
-  Objetos: são conjuntos de pares nome/valor -> {"nome": "João" } (Toda chave é uma string); 
-  null: é um valor especial que representa a ausência de valor

Conseguimos ver a presença de arquivos JSON em configurações do VSCode, por exemplo.

> De Python para JSON, temos o seguinte

|   Python    |  JSON  |
| :---------: | :----: |
|    dict     | object |
| list, tuple | array  |
|     str     | string |
| int, float  | number |
|    True     |  true  |
|    False    | false  |
|    None     |  null  |
