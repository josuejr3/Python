
#### <span style="color:rgb(4, 255, 0)">Relações</span>

![[Pasted image 20250620154927.png]]

Quando falamos de relações, as entidades podem estabelecer até três tipos de relação entre si. (A notação usada é a de pé de galinha).

- Um para um

Nesse caso, um registro de uma tabela está relacionado com um registro de uma outra tabela

	- Não é muito utilizado, pois todos os dados poderiam estar na mesma tabela

	Exemplo: users-profiles, aqui eu "carreguei" a PK de users para FK de profiles.

- Um para muitos

Aqui é quando eu tenho um registro de uma tabela relacionado a muitos registros de outra tabela

	Exemplo: users-profiles, ter vários registros em profiles atrelados ao usuário 1 por exemplo

- Muitos para muitos

		Nesse caso eu não consigo fazer diretamente

		Necessário uma tabela "auxiliar" de meio de caminho

Esse último basicamente é quando muitos registros de uma tabela estão relacionados com muitos registros de uma outra tabela.

