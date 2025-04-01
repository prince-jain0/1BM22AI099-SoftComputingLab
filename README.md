# 1BM22AI099-SoftComputingLab

# Soft Computing Lab - Algorithms Implementation

Welcome to the Soft Computing Lab repository! This project contains implementations of various soft computing and optimization algorithms written in Python. These implementations were developed as part of a lab course to explore and understand key concepts in soft computing, including sorting, optimization, and decision-making techniques.

## Table of Contents
- [Overview](#overview)
- [Algorithms Included](#algorithms-included)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)

## Overview
This repository serves as a collection of practical implementations for a Soft Computing Lab course. The algorithms included demonstrate fundamental techniques in computational intelligence and optimization, such as divide-and-conquer sorting, nature-inspired metaheuristics, and fuzzy logic systems. Each script is self-contained with example usage provided.

## Algorithms Included
1. **Merge Sort**
   - **Description**: A divide-and-conquer sorting algorithm that recursively splits an array into halves, sorts them, and merges them back in sorted order.
   - **File**: `merge_sort.py`
   - **Complexity**: O(n log n)

2a. **Ant Colony Optimization (ACO) for TSP**
   - **Description**: A metaheuristic inspired by ant foraging behavior to solve the Traveling Salesman Problem (TSP). It uses pheromone trails to find an optimal tour.
   - **File**: `aco_tsp.py`
   - **Key Parameters**: Number of ants, iterations, alpha, beta, evaporation rate

2b. **Grey Wolf Optimization (GWO)**
   - **Description**: A metaheuristic inspired by the social hierarchy and hunting behavior of grey wolves to optimize a continuous function (e.g., sphere function).
   - **File**: `gwo.py`
   - **Key Parameters**: Number of wolves, dimensions, maximum iterations

3. **Genetic Algorithm (GA)**
   - **Description**: An evolutionary algorithm that evolves a population of binary chromosomes to maximize a fitness function (here, binary-to-decimal conversion).
   - **File**: `genetic_algorithm.py`
   - **Key Features**: Tournament selection, single-point crossover, mutation, elitism

4. **Fuzzy Logic System**
   - **Description**: A fuzzy logic-based system to determine a tip percentage based on service quality, using triangular membership functions and centroid defuzzification.
   - **File**: `fuzzy_logic.py`
   - **Application**: Decision-making under uncertainty

5. **Particle Swarm Optimization (PSO)**
   - **Description**: A swarm intelligence algorithm that optimizes a continuous function (e.g., sphere function) by adjusting particle positions based on personal and global bests.
   - **File**: `pso.py`
   - **Key Parameters**: Number of particles, dimensions, inertia weight, cognitive/social coefficients


## Requirements
- Python 3.x
- NumPy (`pip install numpy`)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/soft-computing-lab.git
   cd soft-computing-lab
   ```
2. Install the required dependency:
   ```bash
   pip install numpy
   ```

## Usage
Each script can be run independently. Below are instructions for running each algorithm:

### Merge Sort
```bash
python merge_sort.py
```
- **Output**: Sorted array `[1, 2, 3, 4, 5, 6]`

### Ant Colony Optimization (ACO)
```bash
python aco_tsp.py
```
- **Output**: Best tour and total distance for the sample TSP distance matrix.

### Grey Wolf Optimization (GWO)
```bash
python gwo.py
```
- **Output**: Best position and value for the sphere function optimization.

### Genetic Algorithm (GA)
```bash
python genetic_algorithm.py
```
- **Output**: Best chromosome and its fitness value (decimal equivalent).

### Fuzzy Logic System
```bash
python fuzzy_logic.py
```
- **Output**: Suggested tip percentage for a given service quality (e.g., 7.5).

### Particle Swarm Optimization (PSO)
```bash
python pso.py
```
- **Output**: Best position and value for the sphere function optimization.\