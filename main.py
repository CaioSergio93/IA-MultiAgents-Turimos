from crewai import Crew
from textwrap import dedent
from agents import TravelAgents
from tasks import TravelTasks
from dotenv import load_dotenv

load_dotenv()


class TripCrew:
    def __init__(self, origin, cities, date_range, interests):
        self.origin = origin
        self.cities = cities
        self.date_range = date_range
        self.interests = interests

    def run(self):
        # Define os agentes e tarefas personalizados em agents.py e tasks.py
        agents = TravelAgents()
        tasks = TravelTasks()

        # Define seus agentes e tarefas personalizados aqui
        expert_travel_agent = agents.expert_travel_agent()
        city_selection_expert = agents.city_selection_expert()
        local_tour_guide = agents.local_tour_guide()

        # Tarefas personalizadas incluem nome do agente e variáveis como entrada
        plan_itinerary = tasks.plan_itinerary(
            expert_travel_agent, self.cities, self.date_range, self.interests
        )

        identify_city = tasks.identify_city(
            city_selection_expert,
            self.origin,
            self.cities,
            self.interests,
            self.date_range,
        )

        gather_city_info = tasks.gather_city_info(
            local_tour_guide, self.cities, self.date_range, self.interests
        )

        # Defina sua equipe personalizada aqui
        crew = Crew(
            agents=[expert_travel_agent, city_selection_expert, local_tour_guide],
            tasks=[plan_itinerary, identify_city, gather_city_info],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# Esta é a principal função que você usará para executar sua equipe personalizada.
if __name__ == "__main__":
    print("## Bem-vindo ao Trip Planner Crew")
    print("-------------------------------")
    origin = input(
        dedent("""
      De onde você estará viajando?
    """)
    )
    cities = input(
        dedent("""
      Quais são as opções de cidades que você tem interesse em visitar?
    """)
    )
    date_range = input(
        dedent("""
      Qual é o período de datas que você tem interesse em viajar?
    """)
    )
    interests = input(
        dedent("""
      Quais são alguns dos seus interesses e hobbies principais?
    """)
    )

    trip_crew = TripCrew(origin, cities, date_range, interests)
    result = trip_crew.run()
    print("\n\n########################")
    print("## Aqui está o seu Plano de Viagem")
    print("########################\n")
    print(result)