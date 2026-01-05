def decide_action(risk: float):
    if risk < 0.3:
        return "ALLOW"
    elif risk < 0.6:
        return "DELAY"
    elif risk < 0.8:
        return "DEGRADE"
    else:
        return "REJECT"