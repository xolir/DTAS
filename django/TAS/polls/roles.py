from rolepermissions.roles import AbstractUserRole


class Admin(AbstractUserRole):
    available_permissions = {
        'accept_candidates': True,
        'change_role': False,
    }


class Voter(AbstractUserRole):
    available_permissions = {
        'vote_on_poll': True,
        'view_votes': True,
        'change_role': True,

    }


class Candidate(AbstractUserRole):
    available_permissions = {
        'show_user_profile': True,
        'vote_on_poll': True,
        'view_votes': True,
        'change_role': True,

    }