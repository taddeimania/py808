

class Instrument:
    """An instrument contains the name, sound, and speed at which to playback the audio

    Attributes
    ----------
    name : str
        The name to identify the instrument on the sequencer (max length: 10char)
    sound : str
        The sound to print (and say) to the debug output
    speed : int
        The speed at which to output the say command (Can make 'tisk' sound like a hihat if speed is 500)

    Methods
    -------
    None
    """

    def __init__(self, name="", sound="", speed=120):
        if len(name) > 10:
            raise Exception("Name cannot contain more than 10 characters")
        self.name = name
        self.sound = sound
        self.speed = speed
