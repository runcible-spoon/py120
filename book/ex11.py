# Challenge: Create the classes needed to make the following code work as shown:

# Don't worry about ties or whether votes should be singular.

class Election:

    def __init__(self, candidate_dict):
        self._candidate_dict = {candidate: candidate.vote_total for candidate in candidate_dict}


    @property
    def candidate_dict(self):
        return self._candidate_dict

    def display_candidate_and_votes(self):
        return

    def winner(self):
        winning_total = max(self.candidate_dict.values())
        winner = [candidate for candidate in self.candidate_dict.keys() if self.candidate_dict[candidate] == winning_total][0]
        return winner

    def calculate_percentage(self):
        total_election_votes = sum(self.candidate_dict.values())
        return f'{self.candidate_dict[self.winner()] / total_election_votes * 100:.1f}'

    def results(self):
        for candidate in self.candidate_dict:
            print(f'{candidate}: {self.candidate_dict[candidate]} votes')
        print(f'{self.winner()} won: {self.calculate_percentage()}% of votes')


class Candidate:

    def __init__(self, name):
        self._name = name
        self._vote_total = 0

    @property
    def name(self):
        return self._name

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'{repr(self.name)}'

    @property
    def vote_total(self):
        return self._vote_total

    @vote_total.setter
    def vote_total(self, total):
        self._vote_total = total

    def __iadd__(self, vote):
        self.vote_total += vote
        return self


mike_jones = Candidate('Mike Jones')
susan_dore = Candidate('Susan Dore')
kim_waters = Candidate('Kim Waters')

candidates = {
    mike_jones,
    susan_dore,
    kim_waters,
}

votes = [
    mike_jones,
    susan_dore,
    mike_jones,
    susan_dore,
    susan_dore,
    kim_waters,
    susan_dore,
    mike_jones,
]

for candidate in votes:
    candidate += 1

election = Election(candidates)
election.results()

# Output

# Mike Jones: 3 votes
# Susan Dore: 4 votes
# Kim Waters: 1 votes

# Susan Dore won: 50.0% of votes
