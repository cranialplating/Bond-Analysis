# Created by Ryan Holmes on 01/14/22

import numpy as np
import matplotlib.pyplot as plt
from bondclass import Bond


if __name__ == "__main__":

    bond1 = Bond(1000, .04, 6, .03, None)

    print(f"Bond1 price: {bond1.get_pv()} and currently trading at {bond1.get_type()}")
    print(f"Bond1 YTM: {bond1.get_ytm()}")
    print(f"Bond1 Duration: {bond1.get_duration()}\n")

    bond2 = Bond(1000, .02, 8, None, 1010)

    print(f"Bond2 price: {bond2.get_pv()} and currently trading at {bond2.get_type()}")
    print(f"Bond2 YTM: {bond2.get_ytm()}")
    print(f"Bond3 Duration: {bond2.get_duration()}\n")

    bond3 = Bond(1000, .03, 10, None, 950)

    print(f"Bond3 price: {bond3.get_pv()} and currently trading at {bond3.get_type()}")
    print(f"Bond3 YTM: {bond3.get_ytm()}")
    print(f"Bond3 Duration: {bond3.get_duration()}\n")




