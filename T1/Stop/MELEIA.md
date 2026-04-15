Jogo de STOP 
O jogo funciona de forma coordenada, onde o servidor atua como o mestre da partida, gerenciando o sorteio de letras, a sincronização do tempo entre os jogadores e o cálculo da pontuação.

Arquivos
server.py: Responsável por realizar o sorteio das letras, utilizar barreiras para garantir que todos os jogadores comecem e terminem ao mesmo tempo, e processar a lógica de pontuação comparando as respostas recebidas.

client.py: Interface de terminal para o jogador. Recebe a letra sorteada do servidor, solicita o preenchimento dos campos e envia as respostas para avaliação.

Como rodar
1. Configuração

Ajuste a variável HOST para o endereço IP do servidor no cliente.

Parâmetros: O código está pré-configurado para 2 jogadores (N_J) e 3 rodadas (N_R). Estas constantes podem ser alteradas no topo dos código.

2. Execução do Servidor

Acesse o diretório o qual se encontra os arquivos cLient.py e server.py.

Execute python3 server.py.

O servidor entrará em estado de espera e só iniciará a partida após a conexão de todos os N_J jogadores definidos.

3. Execução dos Jogadores

Execute python3 client.py em terminais diferentes, um para cada participante.

Regras e Fluxo
Início: Após a conexão de todos, o servidor sorteia e envia uma letra.

Preenchimento: Os jogadores devem preencher os campos: NOME, CEP, PROFESSOR e COR.

Pontuação:

3 pontos: Resposta válida e única (nenhum outro jogador escreveu igual).

1 ponto: Resposta válida, mas repetida por outro jogador.

0 pontos: Campo vazio ou inválido.

Finalização: O resultado acumulado é exibido após cada rodada e o vencedor é anunciado ao final da última rodada.