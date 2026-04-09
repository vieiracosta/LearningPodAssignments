policies = []

def add_policy(policy):
    policies.append(policy)
    print(f"Policy '{policy}' added.")

def remove_policy(policy):
    if policy in policies:
        policies.remove(policy)
        print(f"Policy '{policy}' removed.")
    else:
        print("Policy not found.")

def list_policies():
    if not policies:
        print("No policies available.")
    else:
        for policy in policies:
            print(policy)

def test():print("bad format")