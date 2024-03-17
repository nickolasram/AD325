from ticketprogram import TicketSimulation

def test_hw101():
    simulation = TicketSimulation()
    simulation.simulateArrivals(5, 5)
    simulation.processTickets()

test_hw101()