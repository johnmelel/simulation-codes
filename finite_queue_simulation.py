import random
import collections

# Data class for storing information about each call
Call = collections.namedtuple('Call', ['id', 'arrival_time', 'server', 'service_start_time', 'service_time', 'delay', 'status'])

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
    """Returns the time until the next call arrives."""
    distribution = [(0.25, 1), (0.40, 2), (0.20, 3), (0.15, 4)]
    return _get_random_time(distribution)

def get_able_service_time():
    """Returns the service time for Able."""
    distribution = [(0.30, 2), (0.28, 3), (0.25, 4), (0.17, 5)]
    return _get_random_time(distribution)

def get_baker_service_time():
    """Returns the service time for Baker."""
    distribution = [(0.35, 3), (0.25, 4), (0.20, 5), (0.20, 6)]
    return _get_random_time(distribution)


class Simulation:
    """
    A class to run a multi-server queue simulation with a finite queue capacity.
    """
    def __init__(self, num_calls=100, queue_capacity=2):
        self.num_calls = num_calls
        self.queue_capacity = queue_capacity
        self.calls = []
        self.queue = collections.deque()
        self.clock = 0
        self.next_arrival_time = 0
        self.able_free_time = 0
        self.baker_free_time = 0
        self.balked_calls = 0

    def run(self):
        """Runs the simulation."""
        for i in range(self.num_calls):
            self.clock = self.next_arrival_time

            # Process the queue first
            self._process_queue()

            # Now handle the new arrival
            if self.able_free_time <= self.clock:
                self._serve_call('Able', i + 1, self.clock)
            elif self.baker_free_time <= self.clock:
                self._serve_call('Baker', i + 1, self.clock)
            else:
                if len(self.queue) < self.queue_capacity:
                    self.queue.append({'id': i + 1, 'arrival_time': self.clock})
                else:
                    self.balked_calls += 1
                    self.calls.append(Call(i + 1, self.clock, None, None, None, None, 'Balked'))

            self.next_arrival_time = self.clock + get_interarrival_time()

    def _process_queue(self):
        """Processes calls waiting in the queue."""
        while len(self.queue) > 0:
            if self.able_free_time <= self.baker_free_time and self.able_free_time <= self.clock:
                call_info = self.queue.popleft()
                self._serve_call('Able', call_info['id'], call_info['arrival_time'], from_queue=True)
            elif self.baker_free_time < self.able_free_time and self.baker_free_time <= self.clock:
                call_info = self.queue.popleft()
                self._serve_call('Baker', call_info['id'], call_info['arrival_time'], from_queue=True)
            else:
                break # No server is free

    def _serve_call(self, server_name, call_id, arrival_time, from_queue=False):
        """Handles the logic of serving a call."""
        if server_name == 'Able':
            service_time = get_able_service_time()
            service_start_time = max(self.clock, self.able_free_time) if from_queue else self.clock
            self.able_free_time = service_start_time + service_time
        else: # Baker
            service_time = get_baker_service_time()
            service_start_time = max(self.clock, self.baker_free_time) if from_queue else self.clock
            self.baker_free_time = service_start_time + service_time

        delay = service_start_time - arrival_time
        self.calls.append(Call(call_id, arrival_time, server_name, service_start_time, service_time, delay, 'Served'))

    def print_results(self):
        """Prints the simulation results."""
        print(f"{'ID':<5}{'Arrival':<10}{'Server':<10}{'Start':<10}{'Service':<10}{'Delay':<10}{'Status':<10}")
        print("-" * 70)
        served_calls = sorted([c for c in self.calls if c.status == 'Served'], key=lambda x: x.id)
        for call in served_calls:
            print(f"{call.id:<5}{call.arrival_time:<10}{call.server:<10}{call.service_start_time:<10}{call.service_time:<10}{call.delay:<10}{call.status:<10}")

        print("\n" + "-" * 70)
        print(f"Total calls processed: {self.num_calls}")
        print(f"Number of balked calls (queue full): {self.balked_calls}")
        print("-" * 70)

def main():
    """
    Main function to run the finite queue simulation.
    """
    print("Running Multi-Server Queue Simulation with Finite Capacity...")
    simulation = Simulation(num_calls=100, queue_capacity=2)
    simulation.run()
    simulation.print_results()

if __name__ == '__main__':
    main()
