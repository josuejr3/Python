
#### <span style="color:rgb(4, 255, 0)">Subprocessos</span>

O módulo subprocess é um módulo que já vem com o Python e ele é usado para executar processos e comandos externos ao programa. 

O método mais simples para atingir esse objetivo é basicamente instanciar o subprocesso e usar um "run", veja no exemplo abaixo. 

```Python
subprocess.run()
```

O método run de um subprocess tem alguns argumentos principais, sendo eles:

-  stdout - redireciona saída;
-  stdin - redireciona entrada;
-  stderr - redireciona erro.

Esses três argumentos se referem a entrada do processo, saída do processo e os erros do processo.

> ~={green}Exemplo=~

Você executa um comando e o comando "cuspiu" um texto. Esse texto é o stdout que veio do comando, porém, pode ocorrer um erro na saída e ai teremos um stderr.

---

Além da trindade principal de argumentos, temos alguns outros que também valem a pena ser destacados.

-  capture_output - captura a saída e erro para uso posterior
-  text - se True, entradas e saídas serão tratadas como texto e automaticamente codificadas ou decodificadas com o conjunto de caracteres padrão da plaatforma (geralmente UTF-8).
-  shell - se True, terá acesso ao shell do sistema. Ao usar shell (True), <mark style="background: #ABF7F7A6;">é recomendado enviar o comando e os argumentos juntos.</mark> 
-  executable - pode ser usado para especificar o caminho do executável que iniciará o subprocesso.

---

Em relação ao retorno do comando run, teremos:

-  stdout, stderr, returncode (normalmente 0 se deu tudo certo) e args;
-  A codificação de caracteres do Windows pode ser diferente. Vale a pena testar: cp1252, cp852, cp850 (ou outros). Linux e mac usam utf_8. 

Testaremos esse módulo com o comando "ping". Esse comando consiste em enviar um sinal para algum IP e após isso ele meio que verifica se o sinal foi recebido corretamente.



































