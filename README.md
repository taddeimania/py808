# py808

## Getting started

In order to use the py808 drum machine you will need to make sure you have `Python 3`. Do a quick check by typing:

```
python3 -V
```

If you see version 3.4 or above then you should be good. This module utilizes `asyncio` which was introduced in version 3.4.

I'm guessing since you're reading this doc that you've already unarchived the module. If you'd like to just jump right in and have fun, you can run the example project called `example.py` by typing:

### macOS? Make sure you've got headphones on!

```
python3 example.py
```

You should see something that looks like this:

```
Boots      |1|0|0|0|1|0|0|0|1|0|0|0|1|0|0|0
And        |0|1|0|1|0|1|0|1|0|1|0|1|0|1|0|1
Cats       |0|0|1|0|0|0|1|0|0|0|1|0|0|0|1|0
Meow       |1|0|0|0|1|0|0|0|1|0|0|0|1|0|0|0

                            X
boots+meow|n|cats|n|boots+meow|n|cats|n|boots+meow
```

... and if you're on a mac, you probably regret running the program.


## Let's have some fun!

You probably want to have a decimal -> binary string converter handy for easily defining your drum patterns but if you don't i've got you covered. Execute this in your terminal:

```
python3 -c 'import sys;x=sys.argv[-1];print("{0:08b}".format(int(x)))' YOUR_INT_HERE
```

Okay with that in hand you should be able to generate some patterns from integers.

### Creating a Pattern

You can create your pattern with any decimal between 0 and 255. Try out some numbers in the above snippet to see if there are any patterns you like. With that number in hand you can define your first pattern.

```
pattern_1 = Pattern(120)
```

If you want to make a "filler" pattern I have created a built in `Rest` pattern you can import and create instead of saying `Pattern(0)`.

### Creating an Instrument

An instrument is how we have some fun. Like you saw above, if you're on macOS you even get the added benefit of hearing your creation through the say command.

The first argument is the title as it will show on the sequencer, the second is the string that will display below the sequencer as a sound (and your speakers), and the last (optional) argument is the speed at which the synthesized voice will say it's word. The higher, the better imo, although it can be fun for really slow droning sounds.

```
kick = Instrument('Boots', 'boots', 400)
```

### Creating a Track

A track is going to bring your instruments and patterns together. Just create a track like so:

```
track_1 = Track(kick, pattern_1)
```

If you have multiple tracks, you can continue to add them as positional arguments after the first pattern.

> NOTE: Do not reuse a pattern. Since python treats Objects as reference types, if you reuse a pattern in a track the pointer tracking will get messed up. This would be a great TODO or Feature enhancement to ensure pattern reuse was safer - but I only had ~ 4 hours on this.

### Putting it all together

Once you've got all of your tracks or just a single track you can create a song by creating a `Song` instance as such:

```
song = Song(240, True, track_1)
```

> Note: All tracks must have the same amount of patterns. IF not an exception will be raised.

The `240` is the BPM, the `True` is because I want it to continually loop, and the tracks can be listed as subsequent positional arguments after.

Want to see / hear what it sounds like?

```
song.start()
```

## Feel free to mess around with it!

It's fairly resilient, but i'm sure there are places where it will break of course. Set the BPM really slow or really fast, layer as many tracks and patterns as you can. I'd love feedback of how this program was stretched to it's limits.

# Tests

If you'd like to run the unit tests included with the project just run the following command:

```
python3 setup.py test
```

That will install `nose` and discover all of the tests in the `tests/` module.

# Thanks

Thanks for checking out this drum sequencer and I can't wait to hear what you think about it.
