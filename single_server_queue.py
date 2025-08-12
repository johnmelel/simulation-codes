import random
import collections

# Data class for storing information about each customer
Customer = collections.namedtuple('Customer', ['id', 'arrival_time', 'service_start_time', 'service_time', 'delay'])

def _get_random_time(probability_distribution):
    """
    Returns a random time based on a given probability distribution.
    """
    r = random.random()
    cumulative_prob = 0
    for prob, time_val in probability_distribution:
        cumulative_prob += prob
        if r < cumulative_prob:
            return time_val
    return time_val

def get_interarrival_time():
    """Returns the time until the next customer arrives."""
    distribution = [(0.25, 1), (0.40, 2), (0.20, 3), (0.15, 4)]
    return _get_random_time(distribution)

def get_service_time():
    """Returns the service time for the server."""
    distribution = [(0.20, 1), (0.40, 2), (0.25, 3), (0.15, 4)]
    return _get_random_time(distribution)


class Simulation:
    """
    A class to run the single-server queue simulation.
    """
    def __init__(self, num_customers=100):
        self.num_customers = num_customers
        self.customers = []
        self.clock = 0
        self.next_arrival_time = 0
        self.server_free_time = 0
        self.server_idle_time = 0

    def run(self):
        """Runs the simulation for the specified number of customers."""
        for i in range(self.num_customers):
            self.clock = self.next_arrival_time

            if self.clock >= self.server_free_time:
                self.server_idle_time += self.clock - self.server_free_time
                service_start_time = self.clock
                delay = 0
            else:
                service_start_time = self.server_free_time
                delay = service_start_time - self.clock

            service_time = get_service_time()
            self.server_free_time = service_start_time + service_time

            self.customers.append(Customer(i + 1, self.clock, service_start_time, service_time, delay))
            self.next_arrival_time = self.clock + get_interarrival_time()

    def print_results(self):
        """Prints the results of the simulation."""
        print(f"{'ID':<5}{'Arrival Time':<15}{'Start Time':<15}{'Service Time':<15}{'Delay':<10}")
        print("-" * 60)
        for customer in self.customers:
            print(f"{customer.id:<5}{customer.arrival_time:<15}{customer.service_start_time:<15}{customer.service_time:<15}{customer.delay:<10}")

        print("\n" + "-" * 60)
        total_delay = sum(c.delay for c in self.customers)
        avg_delay = total_delay / self.num_customers if self.num_customers > 0 else 0
        print(f"Total server idle time: {self.server_idle_time}")
        print(f"Average customer delay: {avg_delay:.2f}")
        print("-" * 60)


def main():
    """
    Main function to run the single-server queue simulation.
    """
    print("Running Single-Server Queue Simulation...")
    simulation = Simulation(num_customers=100)
    simulation.run()
    simulation.print_results()

if __name__ == '__main__':
    main()
