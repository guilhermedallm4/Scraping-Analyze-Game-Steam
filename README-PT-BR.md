# Coletor de Avaliações Steam

## Descrição

Este código é um script Python que coleta dados de avaliações de jogos na plataforma Steam. Ele utiliza a biblioteca Selenium para interagir com um navegador da web, o BeautifulSoup para analisar páginas HTML e expressões regulares (regex) para manipular strings. O código é configurado para ser executado no modo "headless", o que significa que não exibe uma interface gráfica durante a execução.

## Bibliotecas Necessárias

Para executar o código, você precisa ter as seguintes bibliotecas Python instaladas:

- `selenium`: Usada para automatizar interações com o navegador.
- `beautifulsoup4`: Usada para analisar o HTML das páginas da web.
- `re`: Usada para trabalhar com expressões regulares.
- `json`: Usada para ler e escrever dados no formato JSON.
- `unicodedata`: Usada para trabalhar com caracteres Unicode.
  
Você pode instalar as bibliotecas necessárias usando o seguinte comando:

```
pip install selenium
pip install beautifulsoup4
pip install json
pip install unicodedata
```
## Estrutura JSON

Os dados coletados são armazenados em arquivos JSON com a seguinte estrutura:

```json
{
    "recommendProduct": "quantidade de epssoas que acharam util",
    "numberAward": "número de prêmios",
    "classificationPost": "Recomendado ou Não Recomendado",
    "timeRegistered": "tempo registrado",
    "texto": "texto da avaliação",
    "author": "nome do autor",
    "urlPerfil": "URL do perfil do autor"
}

```

## Funcionamento do Código

O código começa configurando um driver da web para o Chrome e navegando até uma página de avaliações de jogos na Steam. Em seguida, ele coleta informações das avaliações, como o status de recomendação, o número de prêmios, a classificação da avaliação, o tempo registrado, o texto da avaliação, o nome do autor e a URL do perfil do autor.

As informações coletadas são armazenadas em uma estrutura JSON, e o código as anexa a um arquivo JSON. Isso permite coletar e analisar dados de avaliações de jogos na Steam de forma eficiente.
