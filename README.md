**Energy Grid Command for InnoEnergy Students UTUM**
Setup instructions, gameplay mechanics, an example of play ASCII terminal output are below. Inspried the iconic Star Trek Unix game.
Clone or Fork the code and save the grid, Captain!
---
# Energy Grid Command - A MicroPython Game for Raspberry Pi Pico
## Overview
**Energy Grid Command** is an educational text-based simulation game designed for students learning programming on the Raspberry Pi Pico. Inspired by the classic 1971 *Star Trek* game, this first iteration reimagines the challenge of managing the European energy grid. Players assume the role of the Captain of the Energy Star Ship Enterprise, tasked with transforming a strained grid to cope with surging renewable energy, skyrocketing industrial demand, and the rise of electric vehicles (EVs). The game runs entirely on the Pico and interacts with a Windows terminal via USB HID or can be run in any online Pi Pico emulator just copy and paste. It offers a way to explore and innovate; you might want to add other factors like reverse flow from solar and wind, skilled workforce at their limits trying to cope with the energy physics while new unfamiliar things like storage, inverters and power conditioners are needed to keep the grid stable, or Cyber risk! with connecting all these things together (=> Klingons..). The grid is in your hands Captain!

### Key Features
- **Educational Focus**: Teaches programming fundamentals such as loops, conditionals, dictionaries, and user input handling for those wanting to start and some base code for those who already do.
- **Real-World Inspiration**: Reflects realistic energy grid challenges, simplified for gameplay.
- **Interactive Gameplay**: Players deploy resources, respond to random events, and maintain grid stability over 80 turns.
- **Visual Feedback**: Features ASCII art and color-coded stability indicators in the terminal. For more advanced students look at the other repos for Pi Zero where graphics look better. That code can also be cloned and forked.
---
## Setup Instructions
To run **Energy Grid Command** on a Raspberry Pi Pico, follow these steps:
### Requirements
- Raspberry Pi Pico with MicroPython installed.
- Thonny IDE (or another MicroPython-compatible IDE).
- A Windows PC with a USB port.
### Installation
1. **Install MicroPython on the Pico**:
   - Download the MicroPython UF2 file from the [official Raspberry Pi documentation](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html).
   - Hold the BOOTSEL button on the Pico, connect it to your PC via USB, and release the button.
   - Drag the UF2 file onto the Pico’s drive to flash MicroPython.

2. **Set Up Thonny**:
   - Download and install Thonny from [thonny.org](https://thonny.org/).
   - Connect the Pico to your PC via USB.
   - In Thonny, go to **Tools > Options > Interpreter** and select **MicroPython (Raspberry Pi Pico)**. Choose the correct port (e.g., COM3 on Windows) and click OK.

3. **Upload the Game**:
   - Open Thonny and create a new file.
   - Copy the game code (`energy_grid_command.py`) into the file.
   - Save it to the Pico as `main.py` (this ensures it runs automatically when the Pico boots).

4. **Run the Game**:
   - Click the "Run" button in Thonny or power cycle the Pico.
   - The game will launch in the Thonny serial console, displaying a welcome message and the initial grid state.

---
## Gameplay Mechanics
As the Captain, your mission is to manage the energy grid across three quadrants over 80 turns (representing 20 years). Each quadrant contains four sectors, and you must deploy resources to keep them stable amidst growing demand and random events.

### Quadrants and Sectors
- **Quadrant A: High Renewable Penetration**  
  Sectors: A1, A2, A3, A4  
  Challenge: Fluctuations from solar and wind energy.  
  Resource: BESS (Battery Energy Storage Systems)

- **Quadrant B: Industrial Zone**  
  Sectors: B1, B2, B3, B4  
  Challenge: High industrial demand.  
  Resource: BESS

- **Quadrant C: Residential Grid**  
  Sectors: C1, C2, C3, C4  
  Challenge: EV-induced harmonic distortions.  
  Resource: Inverters

### Resources
- **BESS (Quadrants A & B)**:  
  - Capacity: 10 MW per unit  
  - Cost: 0.015 billion EUR per unit  

- **Inverters (Quadrant C)**:  
  - Capacity: 10 MW per unit  
  - Cost: 0.005 billion EUR per unit  

### Stability
- Each sector has a required capacity that increases slightly each turn.
- If the deployed capacity is less than the required capacity, the sector is unstable and has a 50% chance of causing a blackout each turn.
- Blackouts deduct 1 billion EUR from your budget.

### Random Events
- There’s a 20% chance per turn that a random sector will experience an event, increasing its required capacity by 50% for that turn.

### Budget and Turns
- Starting Budget: 300 billion EUR
- Turns: 80 (each turn represents 3 months)
- **Victory Condition**: Survive 80 turns with a budget greater than 0 and fewer than 5 blackouts.
- **Defeat Conditions**: Budget reaches 0 or below, or 5 or more blackouts occur.

---

## How to Play
1. **Start the Game**:  
   The game begins with a welcome message and displays the initial state of the grid.

2. **View the State**:  
   Enter `STATUS` to see the current turn, budget, blackout count, and detailed sector information.

3. **Deploy Resources**:  
   Use the command `DEPLOY [BESS|INVERTER] [SECTOR] [QUANTITY]` to allocate resources.  
   Example: `DEPLOY BESS A1 2` deploys 2 BESS units to sector A1.

4. **End Your Turn**:  
   Type `END` to complete your actions and advance to the next turn.

5. **Monitor Stability**:  
   After each turn, the game checks for unstable sectors and reports any blackouts.

6. **Win or Lose**:  
   - **Victory**: Reach turn 80 with budget > 0 and < 5 blackouts.  
   - **Defeat**: Budget ≤ 0 or ≥ 5 blackouts.

### Commands
- `DEPLOY [BESS|INVERTER] [SECTOR] [QUANTITY]`: Deploy resources to a sector.
- `END`: End the current turn and process stability checks.
- `STATUS`: Display the current game state.
- `HELP`: List available commands.

---

## Detailed Example of Play
Example of the first few turns, showing typical player commands and their effects, along with game responses:

### Turn 1
**Initial State:**

```
Welcome to Energy Grid Command!
You are the Captain of the Energy Star Ship Enterprise.
Your mission: Manage the European energy grid for 20 years (80 turns).

Turn: 1, Budget: 300 billion EUR, Blackouts: 0
Quadrant A: High Renewable Penetration
  A1: BESS: 0 units (0 MW), Req: 20.0 MW, Unstable
  A2: BESS: 0 units (0 MW), Req: 20.0 MW, Unstable
  A3: BESS: 0 units (0 MW), Req: 20.0 MW, Unstable
  A4: BESS: 0 units (0 MW), Req: 20.0 MW, Unstable
Quadrant B: Industrial Zone
  B1: BESS: 0 units (0 MW), Req: 15.0 MW, Unstable
  B2: BESS: 0 units (0 MW), Req: 15.0 MW, Unstable
  B3: BESS: 0 units (0 MW), Req: 15.0 MW, Unstable
  B4: BESS: 0 units (0 MW), Req: 15.0 MW, Unstable
Quadrant C: Residential Grid
  C1: Inverters: 0 units (0 MW), Req: 10.0 MW, Unstable
  C2: Inverters: 0 units (0 MW), Req: 10.0 MW, Unstable
  C3: Inverters: 0 units (0 MW), Req: 10.0 MW, Unstable
  C4: Inverters: 0 units (0 MW), Req: 10.0 MW, Unstable
Enter command:
```
**Player Input:**
```
DEPLOY BESS A1 3
```
**Response:**
```
Deployed 3 BESS to A1. Cost: 0.045 billion EUR.
Enter command:
```
**Player Input:**
```
DEPLOY INVERTER C1 2
```
**Response:**
```
Deployed 2 Inverters to C1. Cost: 0.01 billion EUR.
Enter command:
```
**Player Input:**
```
END
```
**Game Response:**
```
Processing turn...
Blackout in A2! Cost: 1 billion EUR.
Blackout in B1! Cost: 1 billion EUR.
Total blackout cost this turn: 2 billion EUR.
```
### Turn 2
**Updated State:**

```
Turn: 2, Budget: 297.945 billion EUR, Blackouts: 2
Quadrant A: High Renewable Penetration
  A1: BESS: 3 units (30 MW), Req: 21.0 MW, Stable
  A2: BESS: 0 units (0 MW), Req: 21.0 MW, Unstable
  A3: BESS: 0 units (0 MW), Req: 21.0 MW, Unstable
  A4: BESS: 0 units (0 MW), Req: 21.0 MW, Unstable
Quadrant B: Industrial Zone
  B1: BESS: 0 units (0 MW), Req: 15.5 MW, Unstable
  B2: BESS: 0 units (0 MW), Req: 15.5 MW, Unstable
  B3: BESS: 0 units (0 MW), Req: 15.5 MW, Unstable
  B4: BESS: 0 units (0 MW), Req: 15.5 MW, Unstable
Quadrant C: Residential Grid
  C1: Inverters: 2 units (20 MW), Req: 10.2 MW, Stable
  C2: Inverters: 0 units (0 MW), Req: 10.2 MW, Unstable
  C3: Inverters: 0 units (0 MW), Req: 10.2 MW, Unstable
  C4: Inverters: 0 units (0 MW), Req: 10.2 MW, Unstable
Event: Increased requirement in A3!
  A3: BESS: 0 units (0 MW), Req: 31.5 MW, Unstable (Event!)
Enter command:
```
**Player Input:**
```
DEPLOY BESS A3 4
```
**Response:**
```
Deployed 4 BESS to A3. Cost: 0.06 billion EUR.
Enter command:
```
**Player Input:**

```
END
```
**Game Response:**
```
Processing turn...
No blackouts this turn.
```
### Turn 3
**Updated State:**

```
Turn: 3, Budget: 297.885 billion EUR, Blackouts: 2
Quadrant A: High Renewable Penetration
  A1: BESS: 3 units (30 MW), Req: 22.0 MW, Stable
  A2: BESS: 0 units (0 MW), Req: 22.0 MW, Unstable
  A3: BESS: 4 units (40 MW), Req: 22.0 MW, Stable
  A4: BESS: 0 units (0 MW), Req: 22.0 MW, Unstable
Quadrant B: Industrial Zone
  B1: BESS: 0 units (0 MW), Req: 16.0 MW, Unstable
  B2: BESS: 0 units (0 MW), Req: 16.0 MW, Unstable
  B3: BESS: 0 units (0 MW), Req: 16.0 MW, Unstable
  B4: BESS: 0 units (0 MW), Req: 16.0 MW, Unstable
Quadrant C: Residential Grid
  C1: Inverters: 2 units (20 MW), Req: 10.4 MW, Stable
  C2: Inverters: 0 units (0 MW), Req: 10.4 MW, Unstable
  C3: Inverters: 0 units (0 MW), Req: 10.4 MW, Unstable
  C4: Inverters: 0 units (0 MW), Req: 10.4 MW, Unstable

Enter command:
```

This example demonstrates deploying resources, handling blackouts, and responding to random events and game flow.

---

## Typical ASCII Terminal Output
Here’s a sample of the game’s terminal output, including color-coded stability indicators (green for stable, red for unstable, in a real terminal):

```
Welcome to Energy Grid Command!
You are the Captain of the Energy Star Ship Enterprise.
Your mission: Manage the European energy grid for 20 years (80 turns).

Turn: 1, Budget: 300 billion EUR, Blackouts: 0
Quadrant A: High Renewable Penetration
  A1: BESS: 0 units (0 MW), Req: 20.0 MW, Unstable
  A2: BESS: 0 units (0 MW), Req: 20.0 MW, Unstable
  A3: BESS: 0 units (0 MW), Req: 20.0 MW, Unstable
  A4: BESS: 0 units (0 MW), Req: 20.0 MW, Unstable
Quadrant B: Industrial Zone
  B1: BESS: 0 units (0 MW), Req: 15.0 MW, Unstable
  B2: BESS: 0 units (0 MW), Req: 15.0 MW, Unstable
  B3: BESS: 0 units (0 MW), Req: 15.0 MW, Unstable
  B4: BESS: 0 units (0 MW), Req: 15.0 MW, Unstable
Quadrant C: Residential Grid
  C1: Inverters: 0 units (0 MW), Req: 10.0 MW, Unstable
  C2: Inverters: 0 units (0 MW), Req: 10.0 MW, Unstable
  C3: Inverters: 0 units (0 MW), Req: 10.0 MW, Unstable
  C4: Inverters: 0 units (0 MW), Req: 10.0 MW, Unstable

Enter command: DEPLOY BESS A1 3
Deployed 3 BESS to A1. Cost: 0.045 billion EUR.

Enter command: DEPLOY INVERTER C1 2
Deployed 2 Inverters to C1. Cost: 0.01 billion EUR.

Enter command: END
Processing turn...
Blackout in A2! Cost: 1 billion EUR.
Blackout in B1! Cost: 1 billion EUR.
Total blackout cost this turn: 2 billion EUR.

Turn: 2, Budget: 297.945 billion EUR, Blackouts: 2
...
```

---

## Customization and Learning Opportunities
Try:
- Tweaking resource costs or capacities.
- Adding new quadrants or resource types.
- Creating more complex random events (e.g., multi-turn weather effects, money, cashflow, the crew saying [whatever] )
- Improving visuals with additional ASCII art.

### Learning Outcomes
- **Programming Skills**: Loops, conditionals, dictionaries, and functions.
- **Microcontroller Use**: Running code on the Pico and interfacing with a PC.
- **Game Design**: Managing game loops, randomness, and player interaction.

---
---
## How Students Start the Serial Console
The easiest way for students to interact with the game is through **Thonny’s serial console**. Here’s how:

1. **Set Up Thonny**:
   - Ensure Thonny is installed on the school PCs (download from [thonny.org](https://thonny.org)).
   - Connect the Pico to the PC via USB.
   - In Thonny, go to **Tools > Options > Interpreter** and select **MicroPython (Raspberry Pi Pico)**.

2. **Run the Game**:
   - Write or load the game script in Thonny.
   - Save it as `main.py` on the Pico.
   - Click the "Run" button to start the game.
   - The serial console will appear in Thonny’s "Shell" window, where students can see output and type commands.

- **Recommendation**:  Impute energy physics (power math) and economics/time (NPV / Calculus) to make it more accurate. Consider latency of turns - buying stuff, backorders from other grids trying to do the same thing in the same timeframe with the same limited suppliers; delivery, where to keep the inventory and cost of that vs cashflow now in your company versus the long term payback of a regulated asset base and workforce to scale it (few qualified engineers to go into high voltage areas, few electronics engineers to work with the equipment and until they do, any AI or platforms using the data will go (very) hungry. This first iteration is just text based and runs without libraries. For more realism it could be run on a Pi Zero with HDMI graphics (in R or Matplotlib) as readout sscreens for Spocks. Pi Zero's can easily be linked over MicroCloud Redis (e.g. AWS t2.nano) which can update all Pi Zeros in near real time but won't store or do the math - do that on the Pi's locally. See other repos for how to do Redis with Pi Zero. Its potentially a decentral game like the grid aspries one day to be: 20 Pi Zeros can be run for about $15 a month on a nano instance; no need for MQTT, SQL or costly processing in a cloud as long as you have decentral users with no need for handling millions of people in a "platform")

---

Enjoy commanding the energy grid, Captains! (you have 300BN to spend in the 80 turns, this can be adjusted too but is a realistic figure, see balance sheets from EU grid companies and add up the next 4 years investments)
