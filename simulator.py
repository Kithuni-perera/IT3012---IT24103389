# simulator.py
from grid_game import GridHuntGame
from agent import GreedyGridAgent

def run_grid_hunt():
    # Create the environment (the 4x4 grid with food and walls) and the agent that will act in it
    env = GridHuntGame()
    agent = GreedyGridAgent()

    print("=== UC Berkeley Style Small Grid Hunt Started ===")
    # Main sense-act-execute loop: keep running until all food is eaten or the step limit is hit
    while not env.is_done():
        # 1. Environment tells the agent what it currently perceives (position, smells, score, etc.)
        percept = env.get_percept(agent)
        # 2. Agent decides on an action based on that percept
        action = agent.sense_and_act(percept)
        # 3. Environment applies the action, updating position/score/food accordingly
        env.execute_action(agent, action)
        # Log the state before the action was executed, so we can see progress each turn
        print(f"Pos: {percept['agent_pos']} | Food Left: {percept['remaining_food']} | Score: {percept['score']}")

    # Loop has ended: either all food was collected or the max step count was reached
    print(f"\nGame Over! Final Score: {env.score} after {env.steps} steps.")


if __name__ == "__main__":
    run_grid_hunt()