import sys
import re

# Initialize the firewall rules list
firewall_rules = []

# Function to validate IPv4 address
def validate_ip(addr):
    ip_pattern = re.compile(r"^(10\.\d{1,3}\.\d{1,3}\.\d{1,3})(-\d{1,3})?$")
    return ip_pattern.match(addr)

# Function to add a rule
def add_rule(rule_number, direction, addr):
    if not validate_ip(addr):
        print(f"Invalid IP address or range: {addr}")
        return

    new_rule = {"rule_number": rule_number, "direction": direction, "addr": addr}
    
    # Check if rule_number is provided, if not assume 1 and shift subsequent rules
    if rule_number is None:
        rule_number = 1
        for rule in firewall_rules:
            rule["rule_number"] += 1
    else:
        for rule in firewall_rules:
            if rule["rule_number"] >= rule_number:
                rule["rule_number"] += 1

    # Insert the rule at the correct position
    firewall_rules.insert(rule_number - 1, new_rule)
    print(f"Rule added: {new_rule}")

# Function to remove a rule
def remove_rule(rule_number, direction=None):
    for rule in firewall_rules:
        if rule["rule_number"] == rule_number:
            if direction:
                if rule["direction"] == direction:
                    firewall_rules.remove(rule)
                    print(f"Removed rule {rule_number} for {direction}")
            else:
                firewall_rules.remove(rule)
                print(f"Removed rule {rule_number}")
            return
    print(f"Rule {rule_number} not found.")

# Function to list rules
def list_rules(rule_number=None, direction=None, addr=None):
    filtered_rules = firewall_rules
    if rule_number:
        filtered_rules = [rule for rule in filtered_rules if rule["rule_number"] == rule_number]
    if direction:
        filtered_rules = [rule for rule in filtered_rules if rule["direction"] == direction]
    if addr:
        filtered_rules = [rule for rule in filtered_rules if rule["addr"] == addr]

    if filtered_rules:
        for rule in filtered_rules:
            print(f"Rule {rule['rule_number']} - {rule['direction']} - {rule['addr']}")
    else:
        print("No matching rules found.")

# Main function to handle commands
def main():
    if len(sys.argv) < 2:
        print("Usage: <add/remove/list> [parameters]")
        return
    
    command = sys.argv[1]
    
    if command == "add":
        if len(sys.argv) < 4:
            print("Usage: add [rule_number] [-in|-out] addr")
            return
        rule_number = None
        if sys.argv[2].isdigit():
            rule_number = int(sys.argv[2])
            direction = sys.argv[3]
            addr = sys.argv[4]
        else:
            direction = sys.argv[2]
            addr = sys.argv[3]
        add_rule(rule_number, direction, addr)

    elif command == "remove":
        if len(sys.argv) < 3:
            print("Usage: remove rule_number [-in|-out]")
            return
        rule_number = int(sys.argv[2])
        direction = sys.argv[3] if len(sys.argv) > 3 else None
        remove_rule(rule_number, direction)

    elif command == "list":
        rule_number = None
        direction = None
        addr = None
        if len(sys.argv) > 2:
            if sys.argv[2].isdigit():
                rule_number = int(sys.argv[2])
            elif sys.argv[2] in ["-in", "-out"]:
                direction = sys.argv[2]
            else:
                addr = sys.argv[2]
        list_rules(rule_number, direction, addr)
    
    else:
        print("Invalid command. Use 'add', 'remove', or 'list'.")

if __name__ == "__main__":
    main()
