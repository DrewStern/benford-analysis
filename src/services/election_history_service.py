from src.services.election_event_service import ElectionEventService
from src.services.election_result_service import ElectionResultService


class ElectionHistoryService:
    def __init__(self, election_event_service: ElectionEventService, election_result_service: ElectionResultService):
        self.election_result_service = election_result_service
        self.election_event_service = election_event_service

    def get_winning_party_history_for_locality(self, locality):
        return self.get_winner_history_for_locality(locality, self.election_result_service.get_winning_party_for_election)

    def get_winning_candidate_history_for_locality(self, locality):
        return self.get_winner_history_for_locality(locality, self.election_result_service.get_winning_candidate_for_election)

    def get_winner_history_for_locality(self, locality, callback):
        years = self.election_event_service.get_election_years()
        winning_candidate_history = dict.fromkeys(years, "")
        county = locality.split(',')[0]
        state = locality.split(',')[1]
        for year in years:
            winning_candidate = callback(year, county, state)
            if winning_candidate != None:
                winning_candidate_history[year] = winning_candidate
        return winning_candidate_history