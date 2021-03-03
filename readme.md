<p>Título: API-Crawler</p>

<p>Autor: Leonardo Araújo</p>

<p>A API foi criada com Node utilizando Flask e Selenium, para fins de estudo.</p>

<p>A API funciona da seguinte maneira:</p>

    A API é composta por uma rota que é responsável pelo
    seu principal funcionamento.

    É uma API que recebe um parametro dish (prato) na rota e a partir
    daí o selenium realiza um crawler no site "Tudo gostoso" fazendo a busca
    atraver do prato escolhido.

        Requisição GET : ttp://127.0.0.1:5000/<dish> (exemplo: dish == bolo)
        // Lista as 3 primeiras receitas correspondentes ao dish.
        // Exemplo:

        {
          "Status": 200,
          "Message": "Essas são as três primeiras receitas de Tudo Gostoso",
          "Receitas": [
            {
              "Title": "BOLO DE AVEIA COM CACAU NO MICRO-ONDAS",
              "Link": "https://www.tudogostoso.com.br/receita/307527-bolo-de-aveia-com-cacau-no-micro-ondas.html",
              "Avatar": "https://img.itdg.com.br/tdg/images/recipes/000/307/527/342452/342452_original.jpg?mode=crop&width=160&height=220"
            },
            {
              "Title": "BOLO DE DOIDO",
              "Link": "https://www.tudogostoso.com.br/receita/307527-bolo-de-aveia-com-cacau-no-micro-ondas.html",
              "Avatar": "https://img.itdg.com.br/tdg/images/recipes/000/179/005/222063/222063_original.jpg?mode=crop&width=160&height=220"
            },
            {
              "Title": "BOLO XADREZ COM BRIGADEIRO",
              "Link": "https://www.tudogostoso.com.br/receita/307527-bolo-de-aveia-com-cacau-no-micro-ondas.html",
              "Avatar": "https://img.itdg.com.br/tdg/images/recipes/000/300/777/321107/321107_original.jpg?mode=crop&width=160&height=220"
            }
          ]
        }
    
    OBS: Caso dish não seja encontrado, o retorno de requisição será:

        {
          "Status": 400,
          "Message": "Receita não encontrada"
        }

<p>Como testar em sua máquina:</p>

    Para testar em sua máquina, basta seguir o passo a passo abaixo.
    Lembrando que aconselha-se a utilizar virtualenv, caso não queira, basta
    ignorar os passos 2 e 3 abaixo:

    Tendo ciência de tudo isso, vamos ao passo a passo:

        1. Clone o repositório em sua máquina e entre na pasta clonada/baixada. (Baixando o ZIP ou pelo GIT);
        2. Tendo o virtualenv instalado, rode o comando "virtualenv <nome-do-env>";
        3. Entre no virtualenv com o comando "source <nome-do-env>/bin/activate";
        4. Tendo o pip e o python instalados rode o comando "pip install -r requirements.txt";
        5. Agora basta rodar o comando "python index.py" e realizar as requisições, passando o
        dish;