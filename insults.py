#!/usr/bin/env python
import random
import sys

if len(sys.argv) >= 2:
    times = int(sys.argv[1])
else:
    times = 1


first = ["FILTHY", "CRUSTY", "RUSTY", "STUPID", "STINKY", "LUMPY", "ROTTEN", "LAZY", "SMELLY", "SQUISHY", "LUMPY", "NO", "GOOD", "BRAINLESS"]
second = ["CRAP", "BUTT", "TURD", "BUM", "POOP", "PUSS", "ROD", "PUKE", "WIENER", "FART", "NUT", "TRASH", "DONG"]
third = ["MAMMOTH", "EXPLORER", "LIZARD", "WIZARD", "TUNNEL", "FAIRY", "HAMSTER", "CAPTAIN", "DRAGON", "WEASEL", "GOBLIN", "PIRATE", "BANJO"]

for x in range(times):
    print("{} {} {}".format(random.choice(first),random.choice(second),random.choice(third)))
