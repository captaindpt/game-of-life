# Conway's Game of Life with Pygame GUI

This Python project implements Conway's Game of Life, a cellular automaton made by mathematician John Conway in 1970. The game is a zero-player game, and users can create an initial configuration and observe how it evolves. Th GUI was made using Pygame.

## Features

- **Interactive Grid**: Click to toggle the state of cells before starting the simulation.
- **Control Buttons**: Buttons to start/pause the simulation, reset the grid to an empty state, and randomize the initial state.
- **Speed Slider**: A slider to adjust the simulation speed.
- **Resizable Grid**: Adjust the `CELL_SIZE` constant to change the grid size.

### Prerequisites

Ensure you have Python 3.6 or newer installed on your system. You can download Python from [python.org](https://www.python.org/).

This project depends on the following Python package:
- Pygame

### Installation

1. Clone the repository to your local machine:
```git clone https://github.com/yourusername/game-of-life-pygame.git```
2. Navigate to the project directory:
```cd game-of-life-pygame```

3. Install the required package using pip:
```pip install pygame```
```pip install numpy```


### Running the Game

To run the game, execute the main Python script from your terminal or command prompt:

```python graphic_renderer.py```

## How to Use

- **Left-Click** on cells to toggle their state between alive (white) and dead (black).
- Use the **Randomize** button to fill the grid with a random pattern. The pattern's density is not user-configurable via the UI but can be adjusted in the code.
- The **Play/Pause** button starts or pauses the simulation.
- The **Reset** button clears the grid, returning it to an all-dead state.
- Adjust the **Speed** with up and down arrow buttons.
