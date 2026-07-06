from agents.root_agent import root_agent

print("=== AI Marketing Operations Manager ===")

print()

print("Root Agent")
print(root_agent.name)

print()

print("Model")
print(root_agent.model)

print()

print("Sub Agents")

for agent in root_agent.sub_agents:
    print("-", agent.name)