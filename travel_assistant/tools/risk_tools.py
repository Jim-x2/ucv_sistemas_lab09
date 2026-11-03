
def assess_basic_travel_risks(destination: str, season: str) -> dict:
    """Evalúa riesgos básicos de viaje según el destino y la temporada."""

    destination_normalized = destination.lower().strip()
    season_normalized = season.lower().strip()

    risks = []

    if "cusco" in destination_normalized or "machu picchu" in destination_normalized:
        risks.append(
            "Considerar la prevención del mal de altura y una aclimatación gradual."
        )

    if "rain" in season_normalized or "lluvia" in season_normalized:
        risks.append(
            "Llevar ropa impermeable y revisar las condiciones de carreteras y rutas."
        )

    if "high" in season_normalized or "alta" in season_normalized:
        risks.append(
            "Reservar hoteles, trenes y entradas con anticipación."
        )

    if not risks:
        risks.append(
            "Revisar el clima, transporte local, requisitos sanitarios y documentación."
        )

    return {
        "status": "success",
        "destination": destination,
        "season": season,
        "risks": risks,
    }
