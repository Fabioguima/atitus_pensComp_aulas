# Pensamento Computacional - Execícios de aula

- [Prof Matheus Jardim Bernardes](https://matheusjardimb.com/)
- [Atitus.edu.br](https://atitus.edu.br/)

Exercícios de aula da disciplina de Pensamento Computacional.

## Sobre mim

**Prazer sou Fábio ;)**

Curso Ciências da Computação na Atitus, estou no primeiro semestre e sempre aproveito as oportunidades de agregar conhecimento!!!

Receita simples de bolo de chocolate:

**Ingredientes:**

2 xícaras de açúcar
1 e 3/4 xícaras de farinha de trigo
3/4 de xícara de cacau em pó
1 e 1/2 colher de chá de fermento em pó
1 e 1/2 colher de chá de bicarbonato de sódio
1 colher de chá de sal
2 ovos
1 xícara de leite integral
1/2 xícara de óleo vegetal
2 colheres de chá de essência de baunilha
1 xícara de água fervente


*Modo de preparo:*

Pré-aqueça o forno a 180°C. Unte uma forma com manteiga e farinha.
Em uma tigela grande, misture o açúcar, a farinha, o cacau, o fermento, o bicarbonato e o sal.


![Samuray boleiro](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.adrenaline.com.br%2Fgames%2Fghost-of-yotei-e-anunciado-e-chega-ao-ps5-em-2025-confira-o-trailer%2F&psig=AOvVaw06EBtA9yLIsjDnKIW10uwp&ust=1745348796439000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJipiJrp6YwDFQAAAAAdAAAAABAE)


## DICAS:

- Entenda completamente o que o exercício solicita ANTES de começar a programar.
- Comece escrevendo um pseudo-código em português para estruturar a lógica que deseja criar.
- Use nomes de variáveis claros e objetivos (prefira ‘nome’ em vez de ‘n’; prefira ‘idade’ em vez de ‘i’).
- Acrescente comentários no código para ajudar a você mesmo.
- Faça testes de mesa para validar a sua lógica: utilize papel e caneta, faça rabiscos!
- Quando trabalhar com listas, preste muita atenção nos limites: avalie se não está tentando acessar uma posição menor
  que zero ou maior que a última posição.

## Fork do projeto

Para criar o seu próprio projeto, clique no botão 'Fork' no topo da tela
em [https://github.com/matheusjardimb/atitus_pensComp_aulas/](https://github.com/matheusjardimb/atitus_pensComp_aulas/).

Após isso, será necessário ativar a execução das 'Actions'. Para isso, acesse o menu 'Actions' no topo da tela e clique
na opção de ativar workflows.

## Testes automatizados

Este repositório está configurado para que os testes automatizados sejam executados a cada novo commit diretamente no
GitHub.

Para mais informações, consulte o arquivo [.github/workflows/tests.yml](.github/workflows/tests.yml).

Para executar os testes em seu computador:

```bash
# Instale as dependências (apenas necessário executar uma vez)
pip install -r requirements.txt

# Execute os testes
pytest
```

## Ao desenvolver no seu computador

Considere instalar o [PyEnv](https://github.com/pyenv/pyenv) para gerenciar múltiplas versões de Python em seu
computador.

A versão de Python sugerida/necessária para executar as atividades deste projeto está no
arquivo [.python-version](.python-version).

Caso esteja usando o [Git](https://git-scm.com/), considere utilizar o pre-commit:

```bash
pre-commit install
```