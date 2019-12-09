import os, pickle

data_folder = os.getcwd() + os.path.sep + "smashers" + os.path.sep

class Scheduler:
    """Pings discord users when tournament is open"""

    def __init__(self, smashers: dict, tournamet: str):
        self.smashers  = smashers
        self.tournamet = tournament

    def prompt_smashers(self, match_name):
        """
        This is called when a new tournament is ready

        Messages all registered smashers 
        """
        for _, smasher in smashers.items():
            smasher.prompt(match_name)

        # TODO log here

    def enroll_smasher(self, disc_id: str, uname: str):
        """
        Called when someone sends !enroll {uname} command

        Saves smasher to file and puts in dict
        """

        # TODO: send confirmation query

        # check if already exists
        if disc_id in self.smashers:
            return "You are already registered as {}!".format(smashers[disc_id])

        new_smasher = new Smasher(disc_id, uname)
        with open(data_folder + disc_id, 'wb') as f:
            pickle.dump(new_smasher, f)

        self.smashers[disc_id] = new_smasher
        return "You are now registered as {}".format(uname)

    def remove_smasher(self, disc_id):
        """Removes smasher from records"""

        # TODO: send confirmation query

        os.remove(data_folder + disc_id)

        self.smashers.pop(disc_id, None)

        return "You have been removed from the record"

    async def register(self, disc_id):
        """Called when smasher responds with !yes to prompt"""
        self.smashers[disc_id].register(tourny_link)
