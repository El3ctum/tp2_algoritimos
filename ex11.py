## Comparando Pilhas e Filas ##

from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    age: int


class ServiceQueue:
    def __init__(self):
        self.queue: list[Customer] = []

    def add_customer(self, customer: Customer) -> None:
        self.queue.append(customer)
        print(f"Costumer {customer.name} add with success")
        return None

    def serve_customer(self) -> Customer | None:
        if not self.queue:
            print("No customers in the queue.")
            return None
        costumer: Customer = self.queue.pop(0)
        print(f"The costumer in service is {costumer.name}")
        return costumer

    def queue_size(self):
        queue_size = len(self.queue)
        return queue_size


if __name__ == "__main__":
    service_queue = ServiceQueue()

    service_queue.add_customer(Customer(name="Alice", age=25))
    service_queue.add_customer(Customer(name="Bob", age=30))
    service_queue.add_customer(Customer(name="Charlie", age=22))

    service_queue.serve_customer()
    service_queue.serve_customer()

    print(f"Number of customers in the queue: {service_queue.queue_size()}")

    service_queue.serve_customer()

    service_queue.serve_customer()
