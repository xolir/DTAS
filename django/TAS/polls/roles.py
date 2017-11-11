from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {
        'accept_candidates': True,
    }


class Voter(AbstractUserRole):
    available_permissions = {
        'vote_on_poll': True,
        'view_votes': True,
    }


class Candidate(AbstractUserRole):
    available_permissions = {
        'show_user_profile': True,
    }