
#### <span style="color:rgb(4, 255, 0)">Internacionalização</span>

A internacionalização é um artificio usado para "traduzir" elementos que desejamos e que aparecem ao longo do código.

-  Alguns sites que podem nos ajudar

	https://docs.python.org/3/library/locale.html
	https://learn.microsoft.com/fr-fr/powershell/module/internationali

```Python
import calendar  
import locale  
  
locale.setlocale(locale.LC_ALL, "ru")  
  
print(calendar.calendar(2025))
```

Nesse caso, se o "" após o primeiro parâmetro for nada, significa que ele usará o idioma padrão do SO.

```Python
locale.setlocale(locale.LC_ALL, "pt_BR.UTF-8")
```


