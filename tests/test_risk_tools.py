from travel_assistant.tools.risk_tools import assess_basic_travel_risks


def test_assess_cusco_high_season_risks():
    result = assess_basic_travel_risks("Cusco", "temporada alta")

    assert result["status"] == "success"
    assert result["destination"] == "Cusco"
    assert any("altura" in risk.lower() for risk in result["risks"])
    assert any("anticipación" in risk.lower() for risk in result["risks"])


def test_assess_risks_default():
    result = assess_basic_travel_risks("Lima", "normal")

    assert result["status"] == "success"
    assert len(result["risks"]) == 1
    assert "clima" in result["risks"][0].lower()