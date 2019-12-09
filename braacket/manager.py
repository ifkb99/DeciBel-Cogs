import os, pickle
from glob import iglob

data_folder = os.getcwd() + os.path.sep + "smashers" + os.path.sep

class Manager:
    """Pings discord users when tournament is open"""

    def __init__(self, tournamet: str):
        self.smashers  = {}
        self.tournamet = tournament

        # reads in all enrolled users on startup
        # files are named after user discord id
        for smasher_file in iglob(data_folder + '*'):
            with open(smasher_file, 'rb') as f:
                # only include discord id as key, not whole path
                self.smashers[smasher_file[smasher_file.rfind(os.path.sep)]+len(os.path.sep):] = pickle.load(f)

    def prompt_smashers(self, match_name):
        """
        This is called when a new tournament is ready

        Messages all enrolled smashers 
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
            return "You are already registered as {}!".format(smashers[disc_id].uname)

        new_smasher = new Smasher(disc_id, uname)
        with open(data_folder + disc_id, 'wb') as f:
            pickle.dump(new_smasher, f)

        self.smashers[disc_id] = new_smasher
        # TODO: log
        return "You are now registered as {}".format(uname)

    def remove_smasher(self, disc_id):
        """Removes smasher from records"""

        # TODO: send confirmation query

        os.remove(data_folder + disc_id)

        self.smashers.pop(disc_id, None)

        # TODO: log

        return "You have been removed from the record"

    async def register(self, disc_id, tourny_id, tourny_name):
        """Called when smasher messages !register to Atilla"""

        # register user in braaket
        # TODO: nav to braaket user entry page
        # TODO: check if user already in braaket
        # TODO: if not, register user

        # TODO: log

        message(disc_id, f"You have been registered for {tourny_name}")
