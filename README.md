# Simulation Codes

This repository contains a collection of codes implementing various simulation problems and methods.

## Available Simulations

This section provides an overview of the simulation models available in this repository.

---

### 1. Able-Baker Customer Care Simulation

This script (`able-baker.py`) simulates a multi-channel queueing system. It models a customer care center with two servers, named Able and Baker, who serve incoming callers. This is a classic example of a discrete-event simulation.

#### How the Simulation Works

The simulation models the process of 100 callers arriving at a customer care center. The core logic is as follows:

1.  **Caller Arrival:** The time between consecutive caller arrivals is determined randomly based on a given probability distribution.
2.  **Server Selection:** When a caller arrives, the system attempts to assign them to a server:
    *   If **Able** is free, Able takes the call.
    *   If Able is busy but **Baker** is free, Baker takes the call.
    *   If both are busy, the caller waits in a queue for the first server to become free.
3.  **Service Time:** The time it takes for Able and Baker to serve a caller is also determined randomly, with each server having their own distinct service time probability distribution.

The simulation tracks several key metrics, including the delay (wait time) for each caller and the total idle time for each server.

#### How to Run

To run the simulation, you need Python installed.

```bash
python able-baker.py
```
