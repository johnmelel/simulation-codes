# Simulation Codes

This repository contains a collection of Python scripts that implement various discrete-event simulation models. These scripts are designed to be educational examples of classic simulation problems.

## Available Simulations

This repository includes the following simulation models:

1.  **Able-Baker Customer Care (Multi-Server Queue)**: A classic multi-server queuing system.
2.  **Single-Server Queue**: A fundamental queuing system with one server.
3.  **Multi-Server Queue with Finite Capacity**: A multi-server system with a limited waiting line.

---

### 1. Able-Baker Customer Care Simulation

This script (`able-baker.py`) simulates a multi-channel queueing system. It models a customer care center with two servers, Able and Baker, who have different service time distributions.

#### How it Works

- **Arrivals**: Callers arrive at random intervals.
- **Server Choice**: Arriving callers are served by Able if free, otherwise by Baker if free.
- **Queue**: If both servers are busy, callers wait in an infinite-capacity queue.
- **Metrics**: The simulation tracks caller delays and server idle time.

The original script has been refactored to use a more modular, class-based design that follows modern Python best practices.

#### How to Run

```bash
python able-baker.py
```

---

### 2. Single-Server Queue Simulation

This script (`single_server_queue.py`) implements a basic single-server queuing system. It is a fundamental model for understanding queuing theory.

#### How it Works

- **Arrivals**: Customers arrive at random intervals.
- **Server**: There is only one server to handle the customers.
- **Queue**: If the server is busy, customers wait in an infinite-capacity queue.
- **Metrics**: The simulation tracks customer delays and server idle time.

#### How to Run

```bash
python single_server_queue.py
```

---

### 3. Multi-Server Queue with Finite Capacity

This script (`finite_queue_simulation.py`) is a variation of the Able-Baker model. It features two servers but introduces a queue with a limited capacity.

#### How it Works

- **Arrivals**: Callers arrive at random intervals.
- **Server Choice**: Servers are chosen based on availability, similar to the Able-Baker model.
- **Finite Queue**: If both servers are busy, callers can wait in a queue of a fixed size.
- **Balking**: If a caller arrives when the queue is full, they "balk"—leave the system without being served.
- **Metrics**: The simulation tracks delays, server utilization, and the number of balked callers.

#### How to Run

```bash
python finite_queue_simulation.py
```
