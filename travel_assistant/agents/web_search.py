
from google.adk.agents import Agent
from google.adk.tools import google_search

web_search_agent = Agent(
    name="web_search_agent",
    model="gemini-3.5-flash-lite",
    description="Busca información actualizada sobre destinos turísticos.",
    instruction="""
    Eres un agente especializado en investigar destinos turísticos.
    Utiliza Google Search para encontrar información actualizada.
    Prioriza fuentes oficiales y confiables.
    No inventes precios ni horarios.
    Responde siempre en español.
    """,
    tools=[google_search],
)