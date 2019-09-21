# automato-simulator
Instruções:
- Para rodar o algoritmo basta usar 'py main.py' no terminal com o mesmo aberto no diretório dos arquivos deste repositório
- Digite 1 para testar palavras no automato
- DIgite 2 para mostrar os estados equivalentes

- Na linha 4 do arquivo existe o comando 'f.init("automato.txt")' 
    - Os estados e transições do autômato devem cadastradas em um arquivo '.txt'
    - No arquivo 'automato.txt' está cadastrado um autômato como exemplo de como os estados devem ser cadastrados
    - É de extrema importância que o modelo seja seguido para o bom funcionamento do algoritmo
    - O arquivo 'modelo.txt' serve como backup para se obter o modelo
    - O autômato pode ser cadastrado no arquivo 'automato.txt'
    - É possível criar outros arquivos de texto para cada autômato, NESTE CASO, a linha 4 deve ser alterada para o nome do novo arquivo de texto a ser lido
        - Exemplo: para ler o arquivo 'exemplo.txt' alinha 4 deve ser 'f.init("exemplo.txt")'
    - É recomendado que todos os arquivos '.txt' fiquem no mesmo diretório
- Começando a leitura das palavras a serem testadas, é possível parar a leitura digitando o comando '/sair'
