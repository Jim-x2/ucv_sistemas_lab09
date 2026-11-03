from google.adk.agents import Agent

from travel_assistant.tools.budget_tools import estimate_trip_budget

budget_agent = Agent(
    name="budget_agent",
    model="gemini-3.5-flash-lite",
    description="Calcula presupuestos estimados para viajes.",
    instruction="""
    Eres un especialista en planificación de presupuestos turísticos.

    Tu responsabilidad es ayudar a los viajeros a estimar sus gastos.

    Reglas:
    1. Utiliza la herramienta estimate_trip_budget para calcular el presupuesto.
    2. Considera el destino, los días de viaje y el presupuesto diario.
    3. Explica que el resultado es una estimación.
    4. No inventes precios exactos de hoteles, vuelos ni restaurantes.
    5. Responde siempre en español.
    """,
    tools=[estimate_trip_budget],
)