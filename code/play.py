"""Run simulations of No Thanks"""

import no_thanks

if __name__ == '__main__':
    num_players = input('How many players?')
    scores = no_thanks.run_simulation(num_players)
    print 'Scores: ', scores
