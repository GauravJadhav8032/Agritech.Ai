from agents.farmer_agent import run_farmer_agent
from agents.weather_agent import run_weather_agent
from agents.market_agent import run_market_agent
from agents.expert_agent import run_expert_agent
from agents.optimizer_agent import run_optimizer_agent

def main():
    print("🌱 AgriSyn Multi-Agent AI System Starting...\n")

    farmer_data = run_farmer_agent()
    weather_data = run_weather_agent()
    market_data = run_market_agent()
    expert_advice = run_expert_agent(farmer_data, weather_data, market_data)
    optimized_plan = run_optimizer_agent(farmer_data, weather_data, expert_advice)

    print("\n✅ Final Recommendation:")
    print(optimized_plan)

if __name__ == "__main__":
    main()
