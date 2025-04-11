def run_optimizer_agent(farmer_data, weather_data, expert_advice):
    return {
        "recommended_crop": expert_advice["crop_recommendation"],
        "irrigation_plan": "Drip irrigation, 3 times/week",
        "pesticide_use": "Eco-friendly neem spray"
    }
