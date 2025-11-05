from crewai import Task
from textwrap import dedent


class TravelTasks:
    def __tip_section(self):
        return "Se você fizer o seu MELHOR TRABALHO, eu te darei uma comissão de $10.000!"

    def plan_itinerary(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
            **Tarefa**: Desenvolver um Roteiro de Viagem de 7 Dias
            **Descrição**: Expanda o guia da cidade para um roteiro de viagem completo de 7 dias com planos
                detalhados para cada dia, incluindo previsões do tempo, sugestões de lugares para comer,
                sugestões de bagagem e um detalhamento do orçamento. Você DEVE sugerir lugares reais para visitar,
                hotéis reais para se hospedar e restaurantes reais para frequentar. Este roteiro deve cobrir
                todos os aspectos da viagem, desde a chegada até a partida, integrando as informações do guia da
                cidade com a logística prática de viagem.

            **Parâmetros**:
            - Cidade: {city}
            - Data da Viagem: {travel_dates}
            - Interesses do Viajante: {interests}

            **Nota**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output=dedent(
                """
                A saída DEVE ser um relatório extenso e visualmente organizado, **usando estritamente formatação Markdown (cabeçalhos, listas, negrito e tabelas)**, incluindo:

                ## 🗺️ Roteiro Completo de 7 Dias em [Nome da Cidade]
                **Período**: [Data de Início] a [Data de Fim]
                **Foco**: [Interesses Principais do Viajante]

                ### 🏨 Sugestão de Hospedagem
                - **Hotel/Pousada**: [Nome do Local] (Link/Endereço)
                - **Tipo/Estilo**: [Descrição Curta]
                - **Custo Estimado**: [Valor por Noite/Total]

                ### ☀️ Previsão do Tempo (Resumo)
                - [Breve resumo do clima esperado para o período]

                ### 💼 Sugestões de Bagagem Essencial
                - [Item 1]
                - [Item 2]
                - [Item 3]

                ### 💰 Detalhamento do Orçamento Estimado (Tabela)
                | Categoria | Custo Estimado (R$) | Notas |
                | :--- | :--- | :--- |
                | Voos/Transporte | [Valor] | [Detalhes] |
                | Hospedagem (7 noites) | [Valor] | [Detalhes] |
                | Alimentação | [Valor] | Média de [Valor] por dia. |
                | Atividades/Entradas | [Valor] | [Detalhes] |
                | **TOTAL ESTIMADO** | **[Valor Total]** | **[Moeda]** |

                ### 📅 Planos Diários Detalhados (Dia 1 ao Dia 7)

                #### **Dia 1: [Tema do Dia, ex: Chegada e Exploração do Centro Histórico]**
                * **Manhã**: [Atividade, ex: Check-in no hotel e café da manhã no... (Restaurante Real)]
                * **Tarde**: [Atividade, ex: Visita ao Museu... (Atração Real)]
                * **Noite**: **Jantar** no [Restaurante Real] (Especialidade: [Prato])

                (Repetir a estrutura acima para os dias 2, 3, 4, 5, 6 e 7)
                """
            ),
        )

    def identify_city(self, agent, origin, cities, interests, travel_dates):
        return Task(
            description=dedent(
                f"""
                **Tarefa**: Identificar a Melhor Cidade para a Viagem
                **Descrição**: Analise e selecione a melhor cidade para a viagem com base em critérios
                    específicos, como padrões climáticos, eventos sazonais e custos de viagem.
                    Esta tarefa envolve comparar várias cidades, considerando fatores como condições
                    climáticas atuais, eventos culturais ou sazonais futuros e despesas gerais de viagem.
                    Sua resposta final deve ser um relatório detalhado sobre a cidade escolhida,
                    incluindo custos reais de voo, previsão do tempo e atrações.

                **Parâmetros**:
                - Origem: {origin}
                - Cidades: {cities}
                - Interesses: {interests}
                - Data da Viagem: {travel_dates}

                **Nota**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output=dedent(
                """
                A saída DEVE ser um relatório bem estruturado, **usando estritamente formatação Markdown (cabeçalhos, listas, negrito e tabelas)**, contendo:

                ## 🎯 Cidade Recomendada: [Nome da Cidade Escolhida]
                **Justificativa Principal**: [Resumo da melhor razão para a escolha]

                ### 📊 Análise Comparativa e Justificativa
                | Critério | [Cidade A] | [Cidade B] | [Cidade C] | **Cidade Escolhida** |
                | :--- | :--- | :--- | :--- | :--- |
                | Clima/Previsão | [Detalhe] | [Detalhe] | [Detalhe] | **[Detalhe e Vantagem]** |
                | Eventos/Atrações | [Detalhe] | [Detalhe] | [Detalhe] | **[Detalhe e Vantagem]** |
                | Custo Geral | [Baixo/Médio/Alto] | [Baixo/Médio/Alto] | [Baixo/Médio/Alto] | **[Nível e Vantagem]** |

                ### ✈️ Logística de Voo (Origem: {origin})
                - **Companhia Aérea Sugerida**: [Nome da Companhia]
                - **Custo Estimado do Voo (Ida e Volta)**: R$ [Valor Real ou Estimado]
                - **Tempo de Voo**: [Horas/Minutos]

                ### ☁️ Condições Climáticas (Período: {travel_dates})
                - **Clima Esperado**: [Ex: Ensolarado, Temperaturas entre X°C e Y°C]
                - **Dicas de Vestuário**: [Breve dica]

                ### 🌟 Destaques da Cidade
                - [Atração Principal 1]
                - [Atração Principal 2]
                - [Motivo Adicional da Escolha]
                """
            ),
        )

    def gather_city_info(self, agent, city, travel_dates, interests):
        return Task(
            description=dedent(
                f"""
                **Tarefa**: Coletar Informações Detalhadas do Guia da Cidade
                **Descrição**: Compile um guia detalhado para a cidade selecionada, reunindo informações sobre
                    atrações principais, costumes locais, eventos especiais e recomendações de atividades diárias.
                    Este guia deve fornecer uma visão geral completa do que a cidade tem a oferecer, incluindo
                    joias escondidas, pontos culturais imperdíveis, marcos que devem ser visitados, previsões do
                    tempo e custos de alto nível.

                **Parâmetros**:
                - Cidade: {city}
                - Interesses: {interests}
                - Data da Viagem: {travel_dates}

                **Nota**: {self.__tip_section()}
        """
            ),
            agent=agent,
            expected_output=dedent(
                """
                A saída DEVE ser um guia detalhado e atrativo, **usando estritamente formatação Markdown (cabeçalhos, listas e negrito)**, incluindo:

                ## 🏙️ Guia da Cidade: [Nome da Cidade]
                **Foco Principal**: [Resumo dos Interesses do Viajante]

                ### ✨ Principais Atrações e Pontos Turísticos
                * **[Nome da Atração 1]**: [Breve descrição e por que visitar]
                * **[Nome da Atração 2]**: [Breve descrição e por que visitar]
                * **[Nome da Atração 3]**: [Breve descrição e por que visitar]

                ### 🎭 Eventos Especiais/Sazonais (Durante o Período da Viagem)
                * [Nome do Evento 1 ou 'Nenhum Evento Principal']
                * [Nome do Evento 2]

                ### 🍽️ Gastronomia e Costumes Locais
                * **Prato Típico Imperdível**: [Nome do Prato] (Onde Provar: [Sugestão de Local])
                * **Dica de Etiqueta/Costume Local**: [Ex: Horário das refeições, gorjeta, etc.]

                ### 💵 Custos Estimados (Alto Nível)
                * **Alimentação Média Diária**: R$ [Valor Estimado]
                * **Transporte Público (Passe Diário)**: R$ [Valor Estimado]
                * **Atrações Turísticas (Custo Médio da Entrada)**: R$ [Valor Estimado]

                ### 🌡️ Previsão do Tempo para {travel_dates}
                * **Temperatura Média**: [Valor]°C
                * **Condição Geral**: [Ensolarado, Chuva, etc.]
                """
            ),
        )