Sistema de Chat (Mensagens)
O sistema é composto por um servidor central e dois tipos de clientes distintos: um para o envio de mensagens e outro exclusivo para a visualização do histórico em tempo real. Porém cada usuário tem cada um desses clientes.

Arquivos
Server.py: Responsável por centralizar todas as conexões, gerenciar a fila de mensagens utilizando semáforos para controle de concorrência e realizar o envio para os clientes visualizadores.

Client.py: Interface de terminal para o usuário realizar sua identificação e enviar textos para o servidor.

Client1.py: Terminal focado em receber e exibir as mensagens formatadas vindas do servidor.

Como rodar
1. Configuração de rede

No Servidor: Recomenda-se configurar a variável HOST como "0.0.0.0" no arquivo Server.py. Isso permite que o serviço aceite conexões de qualquer interface de rede da máquina.

Nos Clientes: O endereço em HOST nos arquivos Client.py e Client1.py deve ser o endereço IP real da máquina onde o servidor está rodando (ou "127.0.0.1" para testes no mesmo computador).

2. Execução do Servidor

Acesse o diretório o qual se encontra os arquivos CLient.py; Client1.py e Server.py.

Execute o comando python3 Server.py.

O sistema utiliza a porta 9002 para a entrada de mensagens e a porta 9003 para a saída (visualização).

3. Visualização

Execute python3 Client1.py para abrir a tela de recebimento.

É recomendável abrir este cliente antes de enviar mensagens para visualizar o histórico completo.

4. Envio

Execute python3 Client.py.

Insira o nome de usuário quando solicitado e digite as mensagens no terminal para transmiti-las.