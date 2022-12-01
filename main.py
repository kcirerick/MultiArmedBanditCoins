from GameMechanics import *
import streamlit as st
"""
Welcome to coin explorer. In this game, your goal is to try to flip as many heads as possible by doing 100 flips of 10 biased coins
whose bias towards landing on heads is uniformly distributed from 0% to 100%. Unfortunately for you, you won't know
what each coin's true bias is, so it will be difficult to know if you are flipping a coin with a 10% bias towards heads
or a 90% bias towards heads. The best you can do is flip the coins and find out! On every turn, you are free to choose any of the 10 coins
to flip. This game involves a little bit of luck, but making good choices can certainly increase your surface area for serendipity!
"""
NUM_COINS = 1
cells = [Cell() for i in range(NUM_COINS)]
for cell in cells:
    button = st.button("Coin")
    st.write(button, on_click = activate_cell(cell))

def activate_cell(cell):
    cell.flipCoin()
    self.getTotalHeads() # Empty values can be assumed to be generic st.write() calls.
    self.getTotalFlips()
    self.getCoinEstimate()
    st.line_chart(self.trend())