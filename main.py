import streamlit as st
import numpy as np

# Set the number of coins and number of flips
NUM_COINS = 10
NUM_FLIPS = 100
NUM_ROWS = 5
NUM_COLS = 2

# Initialize an array to track the number of heads for each coin
heads = np.zeros(NUM_COINS)

# Initialize an array to track the biases of the coins
biases = np.random.rand(NUM_COINS)

# Initialize an array to track the bayesian priors for each coin's bias
priors = np.ones(NUM_COINS) / 2

def update_game():
    pass

def update_line_chart():
    print("Confirmed")

# Create a function to update the bayesian prior for a coin's bias
# based on the number of heads and number of flips for that coin
def update_prior(prior, heads, flips):
    # Compute the probability of getting heads given the current bias
    p_heads = prior * flips
    # Compute the probability of getting tails given the current bias
    p_tails = (1 - prior) * flips
    # Compute the probability of getting the observed number of heads
    p_observed = np.math.comb(flips, int(heads))
    # Update the bayesian prior using Bayes' theorem
    return (p_observed * p_heads) / (p_observed * p_heads + p_observed * p_tails)

# Create a function to flip a coin with a given bias and update the
# number of heads for that coin
def flip_coin(bias, heads):
    pass
    # Flip a coin with the given bias and update the number of heads
    if np.random.rand() < bias:
        heads += 1
    return heads

def create_containers():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.button(
                        label = "H".format(0, 0),
                        key = "Button {}-{}".format(0, 0)
#                         on_click = update_game(),
#                         args = (i, j, line_charts[i][j])
                    )
        with col2:
            st.button(
                                    label = "H".format(0, 1),
                                    key = "Button {}-{}".format(0, 1)
            #                         on_click = update_game(),
            #                         args = (i, j, line_charts[i][j])
                                )
    return #containers, grid

# Create a function to draw the current state of the game
def draw_game(biases, heads, priors):
    #containers, grid = create_containers()
    create_containers()

#     # create a list of line charts, one for each button
#     line_charts = [[
#         st.line_chart([0.5])
#         for j in range(NUM_COLS)]
#     for i in range(NUM_ROWS)]
#
#     # create a grid of buttons
#     button_grid = [[
#         st.button(
#             label = "H".format(i, j),
#             key = "Button {}-{}".format(i, j),
#             on_click = update_game(),
#             args = (i, j, line_charts[i][j])
#         )
#         for j in range(NUM_COLS)]
#     for i in range(NUM_ROWS)]
#
#     for i in range(NUM_ROWS):
#         for j in range(NUM_COLS):
#             st.write(button_grid[i][j])

# Create the main game loop
while True:
    # Draw the current state of the game
    draw_game(biases, heads, priors)
    # Check if the game is over
    if np.sum(heads) == NUM_FLIPS:
        # Compute the total number of heads
        total_heads = np.sum(heads)
        # Compute the total number of tails
        total_tails = NUM_FLIPS - total_heads
        # Show the final results
        st.success(f"Game over! You got {total_heads} heads and {total_tails} tails.")
        # Break out of the loop
        break

