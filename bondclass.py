# Created by Ryan Holmes on 01/14/22

import numpy as np
import math
import matplotlib.pyplot as plt
from scipy.misc import derivative


class Bond:

    def __init__(self, principal, coupon_rate, period, interest, current_price):
        self.principal = principal
        self.coupon_rate = coupon_rate
        self.period = period
        self.interest = interest
        self.schedule = []
        self.current_price = current_price
        self.type = "Par"

        for i in range(period):
            if i == period - 1:
                self.schedule += [principal * (1 + coupon_rate)]
            else:
                self.schedule += [coupon_rate * principal]

        print(f"Successfully Created {self.__class__.__name__} with schedule: {self.schedule}")

    def get_ytm(self, num_iter=6):
        # using Newton's method to find the roots

        if self.interest is not None:
            return self.interest

        calc = [0] * num_iter

        def f(x):
            pv = 0
            for ind, val in enumerate(self.schedule):
                pv += val * (1 + x) ** -(ind + 1)

            return pv - self.current_price

        for n in range(1, num_iter):
            calc[n] = calc[n - 1] - f(calc[n - 1]) / derivative(f, calc[n - 1], dx=1e-6)

        print(f"Newton's Method with {num_iter} iterations: {calc}")

        self.interest = calc[-1]
        return self.interest

    def get_pv(self):

        if self.current_price is not None:
            return self.current_price

        pv = 0
        for ind, val in enumerate(self.schedule):
            pv += val * (1 + self.interest) ** -(ind + 1)

        self.current_price = pv
        return self.current_price

    def get_duration(self):

        if self.current_price is None or self.interest is None:
            print("Error call other methods first")
            return 0

        pv_numerator = 0

        for ind, val in enumerate(self.schedule):
            pv_numerator += (ind + 1) * val * (1 + self.interest) ** -(ind + 1)

        return pv_numerator / self.current_price

    def get_type(self):
        if self.get_pv() < self.principal:
            self.type = "Discount"
        elif self.get_pv() > self.principal:
            self.type = "Premium"
        else:
            self.type = "Par"
        return self.type
