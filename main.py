import streamlit as st
import numpy as np

# Set the number of coins and number of flips
NUM_COINS = 10
NUM_FLIPS = 100
NUM_ROWS = 1
NUM_COLS = 2

# Initialize an array to track the number of heads for each coin
heads, flips = np.zeros(NUM_COINS), np.zeros(NUM_COINS)

# Initialize an array to track the biases of the coins
biases = np.random.rand(NUM_COINS)

# Initialize an array to track the bayesian priors for each coin's bias,
priors = [[0.5] for i in range(NUM_COLS*NUM_ROWS)]

def update_game(button_num, coin_bias):
    result = flip_coin(coin_bias)
    flips[button_num]+=1
    heads[button_num]+=result
    priors[button_num].append(update_prior(priors[button_num][-1], heads[button_num], int(flips[button_num])))
    st.write(priors)

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
    st.write((p_observed * p_heads) / (p_observed * p_heads + p_observed * p_tails))
    return (p_observed * p_heads) / (p_observed * p_heads + p_observed * p_tails)

# Create a function to flip a coin with a given bias and update the
# number of heads for that coin
def flip_coin(bias):
    # Flip a coin with the given bias and update the number of heads
    if np.random.rand() < bias:
        return 1
    return 0

def create_containers():
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            button_num=0
            st.button(
              label = "H",
              key = "Button-{}".format(button_num),
              on_click = update_game,
              args = (button_num, biases[button_num],)
            )
            st.line_chart(priors[0])
        with col2:
            button_num=1
            st.button(
               label = "H",
               key = "Button-{}".format(button_num),
               on_click = update_game,
               args = (button_num, biases[button_num],)
            )
            st.line_chart(priors[1])
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
    break
    if np.sum(heads) == NUM_FLIPS:
        # Compute the total number of heads
        total_heads = np.sum(heads)
        # Compute the total number of tails
        total_tails = NUM_FLIPS - total_heads
        # Show the final results
        st.success(f"Game over! You got {total_heads} heads and {total_tails} tails.")
        # Break out of the loop
        break

