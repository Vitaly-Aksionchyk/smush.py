import shlex
import subprocess
from optimiser.optimiser import Optimiser

class OptimiseAnimatedGIF(Optimiser):
    """
    Optimises animated gifs with Gifsicle - http://www.lcdf.org/gifsicle/
    """

    def __init__(self):
        # the command to execute this optimiser
        self.commands = ("gifsicle -O2 __INPUT__ --output __OUTPUT__",)

        # file extensions this optimiser can work with
        self.extensions = (".gif")

    def _is_acceptable_image(self, input):
        """
        Tests an image to make sure it can be run through this optimiser
        """
        if super(OptimiseAnimatedGIF, self)._is_acceptable_image(input):
            test_command = "identify -format %m " + input
            args = shlex.split(test_command)
            try:
                output = subprocess.check_output(args)
            except OSError:
                print "Error executing command %s. Error was %s" % (test_command, OSError)
                sys.exit(1)

            return output.upper().startswith("GIFGIF")
        
        return False