from Election import *

def standard():
    alex = Elector("Alex")
    mike = Elector("Mike")
    george = Elector("George")

    election = Election([alex,mike,george])
    election.open_polls()

    alex.vote_for(alex,election)
    mike.vote_for(alex,election)
    george.vote_for(george,election)

    election.close_polls()
    winner = election.get_results()
    print ("Winner is " + str(winner) + "!")
