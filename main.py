from agents.root_agent import root_agent

print("=" * 60)
print("AI Marketing Operations Manager")
print("=" * 60)

print("\nAvailable Specialists:")

for agent in root_agent.sub_agents:
    print(f"• {agent.name}")

print("\nType 'exit' to quit.\n")

while True:

    user_input = input("Ask: ")

    if user_input.lower() == "exit":
        print("Goodbye!")
        break

    print("\nUser Question:")
    print(user_input)

    print("\nCoordinator:")
    print("Task received.")
    print("The appropriate specialist(s) will analyze this request.")

    print("\nAvailable Specialists:")

    for agent in root_agent.sub_agents:
        print(f"- {agent.name}")

    print("\n(Response generation will be connected in the next step.)\n")