from crewai import Agent
from textwrap import dedent
import streamlit as st
import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from crewai_tools import SerperDevTool, WebsiteSearchTool
from tools.calculator_tools import CalculatorTools # Mantendo o import caso queira usar a calculadora, mas será preciso adaptar

load_dotenv()

search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()

class TravelAgents:
    def __init__(self):
        # Inicializa o LLM usando ChatOpenAI
        # O modelo 'gpt-3.5-turbo' é o padrão da OpenAI
    
        self.OpenAIGPT35 = ChatOpenAI(
            model="gpt-3.5-turbo", # Modelo padrão da OpenAI
            max_tokens=4000, 
            temperature=0.2
        )

    def expert_travel_agent(self):
        return Agent(
            role="Agente de Viagem Especialista",
            backstory=dedent(
                """Especialista em planejamento de viagens e logística. 
                Tenho décadas de experiência criando roteiros de viagem.
                """
            ),
            goal=dedent("""
                        Criar um roteiro de viagem de 7 dias com planos diários detalhados,
                        incluindo orçamento, sugestões de bagagem e dicas de segurança.
                        """),
            tools=[search_tool, web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def city_selection_expert(self):
        return Agent(
            role="Especialista em Seleção de Cidades",
            backstory=dedent(
                """Especialista em analisar dados de viagem para escolher destinos ideais"""
            ),
            goal=dedent(
                """Selecionar as melhores cidades com base no clima, estação do ano, preços e interesses do viajante"""
            ),
            tools=[search_tool, web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def local_tour_guide(self):
        return Agent(
            role="Guia Turístico Local",
            backstory=dedent("""Guia local conhecedor com informações extensas
        sobre a cidade, suas atrações e costumes"""),
            goal=dedent("""Fornecer os MELHORES insights sobre a cidade selecionada"""),
            tools=[search_tool, web_rag_tool],
            verbose=True,
            llm=self.OpenAIGPT35,
        )
