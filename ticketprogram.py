from queue import Queue
import time
import datetime
import random


class Ticket:
    def __init__(self, ticket_number, timestamp):
        self.ticket_number = ticket_number
        self.timestamp = timestamp

    def to_string(self):
        return f"{self.ticket_number}: {self.timestamp}"


class TicketSimulation:
    def __init__(self):
        self.ticketQueue = Queue()

    # simulate tickets being taken
    # amount: amount of tickets to simulate being taken
    # maxDelta: the maximum amount of seconds between tickets taken
    def simulateArrivals(self, amount, maxDelta):
        for i in range(amount):
            time.sleep(random.randint(0,maxDelta))
            ticket = Ticket(i, datetime.datetime.now().strftime("%H:%M:%S"))
            self.ticketQueue.put(ticket)

    # simulate tickets being processed and empty queue
    def processTickets(self):
        while not self.ticketQueue.empty():
            print(self.ticketQueue.get().to_string())
