class Elector:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
    def vote_for(self, candidate, election):
        ballot = Ballot(candidate)
        election.submit_ballot(self,ballot)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return self.__name

class Ballot:
    def __init__(self, mark):
        self.__mark = mark

    def read(self):
        return self.__mark

class Election:
    def __init__(self, electorate):
        self.__electorate = electorate
        self.__open = False
        self.__already_voted = []
        self.__ballots = {}
    def is_open(self):
        return self.__open

    def open_polls(self):
        self.__open = True

    def close_polls(self):
        self.__open = False
    
    def submit_ballot(self, elector, ballot):
        if not self.is_open():
            raise Exception("Polls Closed")
        elif not elector in self.__electorate:
            raise Exception("Elector Not In Electorate")
        elif elector in self.__already_voted:
            raise Exception("Elector Already Voted")
        else:
            self.__already_voted.append(elector)
            try:
                self.__ballots[ballot.read()] += 1
            except KeyError:
                self.__ballots[ballot.read()] = 1
            return ballot

    def get_results(self):
        if self.is_open():
            raise Exception("Results may be obtained only after polls close")
        winner = None
        count = 0
        tie = False
        for elector in self.__ballots:
            votes = self.__ballots[elector]
            if votes > count:
                winner = elector
                count = votes
                tie = False
            elif votes == count:
                tie = True
            print(elector.get_name() + ": " + str(votes) + " votes.")
        if tie:
            raise Exception("Election Tied")
        else:
            return winner
