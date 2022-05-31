# Tipos de dublês (mocks):

- **Dummy objects:** objeto fictício passado, em geral como parâmetro, mas nunca é usado.

- **Fake objects:** em geral possuem uma implementação que ainda não é adequada para produção (um banco de dados na memória é um bom exemplo).

- **Stubs:** fornecem respostas prontas para as chamadas feitas durante o teste, geralmente não respondendo a nada fora do que está programado para o teste.

- **Spies:** são stubs que registram algumas informações com base em como foram chamados. Por exemplo, um serviço de e-mail que registra quantas mensagens foram enviadas.

- **Mocks:** objetos pré-programados com expectativas que formam uma especificação das chamadas que eles devem receber.
