class Smasher:
    """Data class for each smash member"""
    
    def __init__(self, disc_id, uname):
        self.disc_id = disc_id
        self.uname   = uname

    def prompt(tournament_name):
        """Asks smasher if they will be participating"""
        msg = "Registration is open for {}! Respond with !register and I will register you for the tournament"

        # TODO fake func for now
        message(self.disc_id, msg.format(tournament_name))

    def get_info():
        """Returns smasher info"""
        return self.__dict__

