# Python Challenge

## Question 1

Suponha que um banco possui entre suas APIs de uso interno, as seguintes:
* Um serviço ("Operações em aberto") que gera a cada final de mês, uma lista dos associados e do saldo de suas operações 
financeiras que estão em atraso
* Outro serviço ("Renegociação") que retorna uma lista com os associados que já renegociaram seus atrasos

Suponha que, como parte de uma tarefa, você recebeu o trecho de código em anexo.
A classe *Contract* possui 2 atributos:
* *id*,  o identficador de um correntista e
* *debt*, o saldo devedor total (de todas as operações) de um correntista

Sua tarefa é implementar um método que retorne os *N* maiores devedores que ainda não possuem seus débitos renegociados.
 
O método *get_top_N_open_contracts* possui a assinatura proposta para esta tarefa. Ele recebe 3 parâmetros,
na seguinte ordem:
1. *open_contracts*: Uma lista em que cada elemento é uma instância de *Contract*,
2. *renegotiated_contracts*: Uma lista de numeros inteiros (*int*) representando os identificadores dos associados que já renegociaram seus débitos
3. *top_n*: Um inteiro com a quantidade de devedores que devem ser retornados pelo método.

Por fim, o método deve retornar uma lista contendo *top_n* inteiros referentes aos identificadores dos devedores,
ordenada do maior devedor para o menor, isto é, a posição 0 terá o maior devedor e a posição *top_n* -1 o menor.

Exemplo:
```python
contracts = [
    Contract(1, 1),
    Contract(2, 2),
    Contract(3, 3),
    Contract(4, 4),
    Contract(5, 5)
]
renegotiated = [3]
top_n = 3

actual_open_contracts = get_top_N_open_contracts(contracts, renegotiated, top_n)

expected_open_contracts = [5, 4, 2]
assert expected_open_contracts == actual_open_contracts
```


## Question 2

Suponha que um banco possua um serviço que permita a suas agências fazer requisições de valores monetários (dinheiro)
que serão atendidos por uma central de distribuição através do envio de carros-forte para efetuar as entregas.

Considerado que este banco busca otimizar seus recursos e deseja diminuir a quantidade de viagens de carros-forte,
decidiu-se por unir pedidos de agências próximas a serem entregues na mesma viagem. No entanto, por questões de segurança,
são permitidas a união de no máximo 2 pedidos por viagem e desde que não excedam um valor monetário máximo por viagem.

Sua tarefa é implementar um método que faça o cálculo do número mínimo de viagens, dadas umas lista de requisições
(assuma que cada chamada do método contém apenas requisições de agências próximas) e um valor máximo.

O método *combine_orders*, da classe *Orders*, em anexo possui a assinatura proposta.
* *requests* é uma lista de inteiros, representando o valor monetário requisitado por uma agência.
* *n_max* é um inteiro contendo o valor máximo que pode ser levado em uma única viagem.
* Lembre que cada viagem atende no máximo a 2 requisições.
* Assuma ainda que nenhum valor dentro de *requests* será superior a *n_max*.

Espera-se como retorno apenas um valor inteiro, contendo o número mínimo de viagens que deve ser 
feita para atender todas as requisições.
Não é preciso informar quais requisições serão combinadas, apenas a quantidade mínima de viagens.

Ex:
```python
orders = [70, 30, 10]
n_max = 100
expected_orders = 2

how_many = Orders().combine_orders(orders, n_max)

assert how_many == expected_orders
```


## Pontos extras
Esperamos que o teste seja entregue como um projeto e que o candidato tenha todas as preocupações, com o código, tais como, mas não limitado a:
- Uso de boas práticas
- Aderência aos padrões da linguagem
- Documentação
- Performance da sua solução em diferentes cenários

e não apenas a implementação do método

Em resumo, pedimos que a solução seja uma que o candidato considere de boa qualidade em sua própria definição.

