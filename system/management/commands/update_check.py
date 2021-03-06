# Ghiro - Copyright (C) 2013-2016 Ghiro Developers.
# This file is part of Ghiro.
# See the file 'docs/LICENSE.txt' for license terms.

from optparse import make_option
from django.core.management.base import NoArgsCommand

from ghiro.common import check_version


class Command(NoArgsCommand):
    """Checks for new Ghiro releases."""

    help = "Checks for new Ghiro releases"

    option_list = NoArgsCommand.option_list + (
        make_option("-f", "--force", action="store_true", dest="force"),
    )

    def handle(self, *args, **options):
        """Runs command."""

        print("Starting update check...")

        # If force is enabled we don't use cached response.
        if options["force"]:
            print("Enabled forced check.")
            force = True
        else:
            force = False

        try:
            new_release = check_version(force=force)
        except Exception as e:
            print("Error occurred: %s" % e)
        else:
            if new_release:
                print("New release available!")
            else:
                print("No new releases available.")