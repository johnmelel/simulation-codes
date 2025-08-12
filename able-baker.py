import random
import collections

# Data class for storing information about each call
Call = collections.namedtuple('Call', ['id', 'arrival_time', 'server', 'service_start_time', 'service_time', 'delay'])

def _get_random_time(probability_distribution):
    """
    Returns a random time based on a given probability distribution.

    The distribution is a list of tuples, where each tuple contains
    a probability and a corresponding time value.
    """
    r = random.random()
    cumulative_prob = 0
    for prob, time_val in probability_distribution:
        cumulative_prob += prob
        if r < cumulative_prob:
            return time_val
    # This part should ideally not be reached if probabilities sum to 1,
    # but as a fallback, return the last value.
    return time_val

def get_interarrival_time():
    """Returns the time until the next call arrives."""
    # Probabilities: 0.25, 0.40, 0.20, 0.15
    distribution = [(0.25, 1), (0.40, 2), (0.20, 3), (0.15, 4)]
    return _get_random_time(distribution)

def get_able_service_time():
    """Returns the service time for Able."""
    # Probabilities: 0.30, 0.28, 0.25, 0.17
    distribution = [(0.30, 2), (0.28, 3), (0.25, 4), (0.17, 5)]
    return _get_random_time(distribution)

def get_baker_service_time():
    """Returns the service time for Baker."""
    # Probabilities: 0.35, 0.25, 0.20, 0.20
    distribution = [(0.35, 3), (0.25, 4), (0.20, 5), (0.20, 6)]
    return _get_random_time(distribution)


class Simulation:
    """
    A class to run the Able-Baker simulation.
    """
    def __init__(self, num_calls=100):
        self.num_calls = num_calls
        self.calls = []
        self.clock = 0
        self.next_arrival_time = 0
        self.able_free_time = 0
        self.baker_free_time = 0
        self.able_idle_time = 0
        self.baker_idle_time = 0

    def run(self):
        """Runs the simulation for the specified number of calls."""
        for i in range(self.num_calls):
            self.clock = self.next_arrival_time

            # Update server idle times based on when they become free
            if self.clock >= self.able_free_time:
                self.able_idle_time += self.clock - self.able_free_time
                self.able_free_time = self.clock
            if self.clock >= self.baker_free_time:
                self.baker_idle_time += self.clock - self.baker_free_time
                self.baker_free_time = self.clock

            # Determine which server takes the call
            if self.able_free_time <= self.clock:  # Able is free
                server = 'Able'
                service_time = get_able_service_time()
                service_start_time = self.clock
                self.able_free_time = service_start_time + service_time
                delay = 0
            elif self.baker_free_time <= self.clock:  # Baker is free
                server = 'Baker'
                service_time = get_baker_service_time()
                service_start_time = self.clock
                self.baker_free_time = service_start_time + service_time
                delay = 0
            else:  # Both are busy, caller waits for the first available server
                if self.able_free_time <= self.baker_free_time:
                    server = 'Able'
                    service_time = get_able_service_time()
                    service_start_time = self.able_free_time
                    self.able_free_time += service_time
                else:
                    server = 'Baker'
                    service_time = get_baker_service_time()
                    service_start_time = self.baker_free_time
                    self.baker_free_time += service_time
                delay = service_start_time - self.clock

            self.calls.append(Call(i + 1, self.clock, server, service_start_time, service_time, delay))
            self.next_arrival_time = self.clock + get_interarrival_time()

    def print_results(self):
        """Prints the results of the simulation in a formatted table."""
        print(f"{'ID':<5}{'Arrival Time':<15}{'Server':<10}{'Start Time':<15}{'Service Time':<15}{'Delay':<10}")
        print("-" * 70)
        for call in self.calls:
            print(f"{call.id:<5}{call.arrival_time:<15}{call.server:<10}{call.service_start_time:<15}{call.service_time:<15}{call.delay:<10}")

        print("\n" + "-" * 70)
        print(f"Total idle time for Able: {self.able_idle_time}")
        print(f"Total idle time for Baker: {self.baker_idle_time}")
        print("-" * 70)


def main():
    """
    Main function to initialize and run the Able-Baker simulation.
    """
    print("Running Able-Baker Customer Care Simulation...")
    simulation = Simulation(num_calls=100)
    simulation.run()
    simulation.print_results()

if __name__ == '__main__':
    main()
