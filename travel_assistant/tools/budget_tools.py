def estimate_trip_budget(
    destination: str,
    days: int,
    daily_budget_usd: float
) -> dict:
    """Calcula el presupuesto estimado de un viaje."""

    if days <= 0:
        return {
            "status": "error",
            "message": "Los días deben ser mayores que cero."
        }

    if daily_budget_usd <= 0:
        return {
            "status": "error",
            "message": "El presupuesto diario debe ser mayor que cero."
        }

    total = days * daily_budget_usd

    return {
        "status": "success",
        "destination": destination,
        "days": days,
        "daily_budget_usd": daily_budget_usd,
        "estimated_total_usd": total
    }