🚀 Sistema de Monitoramento Operacional de Missão Espacial
📋 Sobre o Projeto

O Sistema de Monitoramento Operacional de Missão Espacial foi desenvolvido para simular o acompanhamento de uma missão espacial experimental, permitindo a análise de telemetria, monitoramento de recursos críticos, geração automática de alertas e simulação de cenários operacionais.

O projeto aplica conceitos fundamentais de Estruturas de Dados, Algoritmos e Programação em Python, utilizando listas, filas, pilhas, dicionários e matrizes para organizar e processar informações da missão.

Além do monitoramento em tempo real, o sistema oferece recursos de previsão energética, análise de tendências, detecção de inconsistências e visualização gráfica dos indicadores operacionais.

🎯 Objetivos
Simular o monitoramento de uma missão espacial.
Processar dados de telemetria em estruturas computacionais adequadas.
Classificar automaticamente o estado operacional da missão.
Gerar alertas críticos baseados em regras de negócio.
Fornecer recomendações para mitigação de riscos.
Realizar previsões e análises de tendência.
Exibir dashboards gráficos para apoio à tomada de decisão.
⚙️ Funcionalidades
🛰 Painel Operacional
Diagnóstico automático da missão.
Classificação dos estados:
NORMAL
ALERTA
CRÍTICO
EMERGÊNCIA TOTAL
Exibição de alertas críticos.
Detecção de inconsistências operacionais.
Recomendações automáticas.
Previsão de consumo energético.
Análise de tendência de consumo.
📊 Telemetria e Análises
Cálculo da variação energética.
Média de temperatura da missão.
Exibição da hierarquia dos sistemas monitorados.
📚 Eventos da Missão
Histórico de eventos operacionais.
Organização dos eventos utilizando estrutura de pilha.
🔄 Simulação Operacional
Atualização dinâmica dos parâmetros da missão.
Simulação de múltiplos ciclos operacionais.
Reavaliação automática do status da missão.
📈 Dashboard Gráfico

Visualização dos seguintes indicadores:

Energia gerada
Energia consumida
Temperatura
Níveis de radiação
Reserva energética
🏗 Estruturas de Dados Utilizadas
Estrutura	Aplicação
Lista	Histórico de telemetria
Fila (Queue)	Gerenciamento de alertas
Pilha (Stack)	Histórico de eventos
Dicionário	Organização dos módulos e hierarquia
Matriz/Tabela	Análises de indicadores
📂 Estrutura do Projeto
📦 projeto
│
├── main.py
├── monitoramento.py
├── dados_missao.json
│
└── modulos
    ├── alertas.py
    ├── analise_matriz.py
    ├── diagnostico.py
    ├── eventos.py
    ├── graficos.py
    ├── hierarquia.py
    ├── inconsistencias.py
    ├── previsao.py
    ├── recomendacoes.py
    ├── simulacao.py
    └── tendencia.py
🛠 Tecnologias Utilizadas
Python 3.x
JSON
Matplotlib
Tabulate
📦 Instalação

Clone o repositório:

git clone https://github.com/seu-usuario/seu-repositorio.git

Acesse a pasta do projeto:

cd seu-repositorio

Instale as dependências:

pip install matplotlib tabulate
▶️ Como Executar

Execute o arquivo principal:

python main.py
🧠 Lógica de Diagnóstico

O sistema avalia continuamente indicadores críticos da missão:

Reserva de energia
Nível de radiação
Qualidade da comunicação
Estado dos módulos operacionais

Com base nesses parâmetros, o sistema determina automaticamente o status da missão e gera alertas quando necessário.

🔍 Análises Implementadas
Previsão Energética

Calcula uma projeção futura da reserva energética utilizando a média dos últimos consumos registrados.

Tendência de Consumo

Determina se o consumo energético está:

Em aumento
Em redução
Estável
Detecção de Inconsistências

Identifica situações anormais como:

Comunicação desligada com sinal elevado.
Energia fora dos limites aceitáveis.
Radiação extrema sem proteção adequada.
📈 Exemplo de Indicadores Monitorados
Indicador	Valor
Reserva de Energia	48%
Radiação	88
Comunicação	78
Temperatura Média	23°C
💡 Diferenciais do Projeto
Arquitetura modular.
Simulação dinâmica da missão.
Geração automática de alertas.
Dashboard gráfico integrado.
Aplicação prática de estruturas de dados.
Código organizado e de fácil manutenção.
👨‍💻 Equipe

Projeto desenvolvido para o desafio acadêmico de monitoramento operacional de missão espacial.

🤖 Uso de Inteligência Artificial

A Inteligência Artificial foi utilizada como ferramenta de apoio para:

Organização da documentação.
Revisão textual.
Sugestões de estruturação do projeto.
Apoio conceitual durante o desenvolvimento.

Todo o código, lógica implementada e validações foram analisados e compreendidos pela equipe responsável pelo projeto.

📄 Licença

Este projeto possui finalidade educacional e acadêmica.
