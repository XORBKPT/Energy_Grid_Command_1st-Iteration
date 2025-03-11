# Energy Grid Command - A MicroPython game for Raspberry Pi Pico
# Players manage an energy grid across three quadrants over 80 turns
# Deploy BESS (Battery Energy Storage Systems) and Inverters to maintain stability
# Runs in Thonny's serial console with ASCII output and user input

import random

# --- Game Functions ---

def required_bess_a(turn):
    """Calculate required BESS capacity (MW) for Quadrant A sectors."""
    return 20 + 1 * turn  # Increases by 1 MW per turn

def required_bess_b(turn):
    """Calculate required BESS capacity (MW) for Quadrant B sectors."""
    return 15 + 0.5 * turn  # Increases by 0.5 MW per turn

def required_inverters_c(turn):
    """Calculate required Inverter capacity (MW) for Quadrant C sectors."""
    return 10 + 0.2 * turn  # Increases by 0.2 MW per turn

def display_state(state):
    """Display the current game state in the serial console with ANSI colors."""
    print(f"\nTurn: {state['turn']}, Budget: {state['budget']} billion EUR, Blackouts: {state['blackouts']}")
    
    # Display each quadrant and its sectors
    for quad in ['A', 'B', 'C']:
        if quad == 'A':
            print("Quadrant A: High Renewable Penetration")
        elif quad == 'B':
            print("Quadrant B: Industrial Zone")
        else:
            print("Quadrant C: Residential Grid")
        
        for sector in [f"{quad}{i}" for i in range(1, 5)]:
            if quad in ['A', 'B']:
                # Calculate deployed and required capacity for BESS
                deployed = state['deployed'][sector]['BESS'] * 10  # Each unit is 10 MW
                required = required_bess_a(state['turn']) if quad == 'A' else required_bess_b(state['turn'])
            else:  # Quadrant C
                # Calculate deployed and required capacity for Inverters
                deployed = state['deployed'][sector]['Inverters'] * 10
                required = required_inverters_c(state['turn'])
            
            # Adjust required capacity if there's an event
            event_flag = sector in state['events']
            if event_flag:
                required *= 1.5  # 50% increase due to event
            
            # Determine stability with color coding
            stability = "Stable" if deployed >= required else "Unstable"
            color = "\033[32m" if stability == "Stable" else "\033[31m"  # Green or Red
            
            # Display sector info
            resource = 'BESS' if quad in ['A', 'B'] else 'Inverters'
            units = state['deployed'][sector][resource]
            event_text = " (Event!)" if event_flag else ""
            print(f"  {sector}: {resource}: {units} units ({deployed} MW), Req: {required} MW, {color}{stability}\033[0m{event_text}")
    
    # Show active events
    if state['events']:
        print("Active Events:")
        for sector in state['events']:
            print(f"  {sector}: Increased requirement!")

def process_command(command, state):
    """Process user input commands and update the game state."""
    parts = command.split()
    if not parts:
        return False  # No command entered
    
    cmd = parts[0]
    if cmd == "END":
        return True  # End the turn
    
    elif cmd == "DEPLOY":
        if len(parts) != 4:
            print("Invalid command. Use: DEPLOY [BESS|INVERTER] [SECTOR] [QUANTITY]")
            return False
        
        resource, sector, qty_str = parts[1], parts[2], parts[3]
        
        # Validate quantity
        try:
            quantity = int(qty_str)
            if quantity <= 0:
                raise ValueError
        except ValueError:
            print("Quantity must be a positive integer.")
            return False
        
        # Validate resource and sector
        valid_sectors = state['deployed'].keys()
        if resource not in ["BESS", "INVERTER"]:
            print("Invalid resource. Use BESS or INVERTER.")
        elif sector not in valid_sectors:
            print(f"Invalid sector. Valid sectors: {', '.join(valid_sectors)}")
        elif (resource == "BESS" and sector[0] not in ['A', 'B']) or (resource == "INVERTER" and sector[0] != 'C'):
            print(f"Cannot deploy {resource} to {sector}. BESS for A/B, INVERTER for C.")
        else:
            # Calculate cost
            cost = (0.015 if resource == "BESS" else 0.005) * quantity  # BESS: 15M€, Inverter: 5M€
            if state['budget'] >= cost:
                state['deployed'][sector][resource] += quantity
                state['budget'] -= cost
                print(f"Deployed {quantity} {resource} to {sector}. Cost: {cost} billion EUR.")
            else:
                print("Not enough budget.")
        return False
    
    elif cmd == "STATUS":
        display_state(state)
        return False
    
    elif cmd == "HELP":
        print("Commands:")
        print("  DEPLOY [BESS|INVERTER] [SECTOR] [QUANTITY] - Deploy resources")
        print("  END - End the turn")
        print("  STATUS - Show current state")
        print("  HELP - Show this message")
        return False
    
    else:
        print("Unknown command. Type HELP for commands.")
        return False

def check_stability(state):
    """Check stability and apply blackouts if sectors are unstable."""
    blackout_cost = 0
    for sector in state['deployed']:
        if sector[0] in ['A', 'B']:
            deployed = state['deployed'][sector]['BESS'] * 10
            required = required_bess_a(state['turn']) if sector[0] == 'A' else required_bess_b(state['turn'])
        else:
            deployed = state['deployed'][sector]['Inverters'] * 10
            required = required_inverters_c(state['turn'])
        
        if sector in state['events']:
            required *= 1.5
        
        if deployed < required and random.random() < 0.5:  # 50% chance of blackout
            blackout_cost += 1
            state['blackouts'] += 1
            print(f"Blackout in {sector}! Cost: 1 billion EUR.")
    
    state['budget'] -= blackout_cost
    if blackout_cost > 0:
        print(f"Total blackout cost this turn: {blackout_cost} billion EUR.")

# --- Main Game ---

# Initialize game state
sectors = [f"{quad}{i}" for quad in ['A', 'B', 'C'] for i in range(1, 5)]
state = {
    'turn': 0,
    'budget': 300,  # Starting budget in billion EUR
    'blackouts': 0,
    'deployed': {sector: {'BESS': 0, 'Inverters': 0} for sector in sectors},
    'events': []
}

# Welcome message
print("Welcome to Energy Grid Command!")
print("You are the Captain of the Energy Star Ship Enterprise.")
print("Manage the European energy grid over 80 turns.")
print("Deploy BESS (A, B) and Inverters (C) to maintain stability.")
print("Commands: DEPLOY [BESS|INVERTER] [SECTOR] [QUANTITY], END, STATUS, HELP")
print("Good luck, Captain!\n")

# Game loop
max_turns = 80
max_blackouts = 5
while state['turn'] < max_turns and state['budget'] > 0 and state['blackouts'] < max_blackouts:
    state['turn'] += 1
    
    # Random event (20% chance)
    if random.random() < 0.2:
        event_sector = random.choice(sectors)
        state['events'].append(event_sector)
        print(f"Event: Increased requirement in {event_sector}!")
    
    # Show current state
    display_state(state)
    
    # Player input loop
    while True:
        command = input("\nEnter command: ").strip().upper()
        if process_command(command, state):
            break  # END command received
    
    # Check stability after turn
    check_stability(state)
    state['events'] = []  # Clear events for next turn

# Game end
print("\nGame Over!")
if state['turn'] >= max_turns:
    if state['budget'] > 0 and state['blackouts'] < max_blackouts:
        print("Victory! You have successfully managed the energy grid.")
    else:
        print("Defeat. The grid collapsed due to budget or blackouts.")
elif state['budget'] <= 0:
    print("Defeat. Budget depleted.")
else:
    print(f"Defeat. Too many blackouts ({state['blackouts']}).")
