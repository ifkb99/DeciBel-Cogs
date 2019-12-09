class Smasher:
    """Data class for each smash member"""
    
    def __init__(self, disc_id, uname):
        self.disc_id = disc_id
        self.uname   = uname

    def prompt(tournament_id, tournament_name):
        """Asks smasher if they will be participating"""
        msg = "Would you like me to register you for {}?"

        # TODO fake func for now
        message(self.disc_id, msg.format(tournament_name))

    async def register(self, tournament_link, tournament_name):
        """Signs smasher up for event"""
        
        # send packet to braacket
        try:
            # TODO
            # send request / nav to page and sign up
            return "You have been registered for {}, have fun!"

        # if success, return success msg

        # else, return link to braaket and failure msg
        # TODO: write to log
        return "Sorry! Something went wrong. Sign yourself up here: {}".format(tournament_link)
