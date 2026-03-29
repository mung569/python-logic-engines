# Python Logic Engines: Matrix & Behavioral Simulations
This repository features a collection of Python-based engines focused on algorithmic efficiency, 2D-matrix traversal, and automated file processing. Originally developed in late 2025 as part of an intensive programming curriculum, these projects have been refactored to demonstrate a transition from procedural logic to professional-grade pattern matching and structured data management.

## 🚀 Projects Overview

### [Lexical Pattern-Matching Engine](./lexical-pattern-engine/)
An algorithmic tool designed to resolve word-grid puzzles through coordinate-based matrix traversal.
* **Key Focus:** 2D Array manipulation, multi-directional search algorithms, and JSON serialization.
* **Status:** Functional CLI utility with external file I/O.

### [Aether-Triad: Logic Simulator](./aether-triad/)
A terminal-based simulation built around a triadic relationship model (Phoenix-Mage-Warrior).
* **Key Focus:** Input validation, global state management, and modular function design.
* **Status:** Interactive CLI game with randomized opponent logic.

---

## 🛠️ Core Technical Competencies
Across these projects, the following software engineering principles are implemented:

* **Data Structures:** Implementation of 2D Lists (Matrices), Dictionaries, and Sets for efficient data mapping.
* **Algorithmic Logic:** Designing search patterns across 8 potential axes (horizontal, vertical, and reverse).
* **File I/O & Persistence:** Parsing raw `.txt` data and exporting results to structured `.json` for API-ready consumption.
* **Robust Programming:** "Crash-proof" user input handling using Pythonic error-checking and loops.

---

## 📂 Directory Structure
```text
python-foundations/
├── assets/                 # Global screenshots and demos
├── aether-triad/           # Role-based logic simulation
└── lexical-pattern-engine/ # Matrix search and JSON exporter
```

---

## 🛠️ Installation & Execution

These engines are built using **Python 3.x** and utilize standard libraries, requiring no external dependencies (like `pip`) to run.

### 1. Clone the Repository
```bash
git clone [https://github.com/mung569/python-logic-engines.git](https://github.com/mung569/python-logic-engines.git)
cd python-logic-engines
```

### 2. Run the Engines

#### Lexical Pattern-Matching Engine
Processes the wordpuzzle.txt grid and exports coordinates to a JSON file.
```bash
cd lexical-pattern-engine
python word_search_solver.py
```

#### Aether-Triad: Logic Simulator
Starts an interactive, terminal-based behavioral simulation.
```bash
cd aether-triad
python aether_triad.py
```

---

## 📊 Expected Output
* **Lexical Engine:** Displays the character matrix in the terminal and generates a word_search_results.json file in the project folder.

* **Aether-Triad:** Launches an interactive menu for role selection and real-time score tracking against the automated opponent.
