# Dependencies
import time


class CoinProblem:

    def __init__(self, cfg):
        # Initializer of the CoinProblem class
        #

        # Args:
        #   cfg: configuration (.yaml) file

        self.coin_value_list = cfg['inputs']['available_coins']
        self.cash = cfg['inputs']['change']
        self.timer = cfg['inputs']['timer']
        self.experiment = cfg['experiment']
        print('Welcome to the ', self.experiment, '\n')
        self.next_layer = []
        self.output = []
        self.coins = []
        self.stop = False

    def layer_init(self):
        # Function that initialize the
        # base layer of the the Tree

        init_layer = []

        # Iterate over every available coin
        for coin in self.coin_value_list:

            # We append every coin in the layer
            # we use it two times because the cash
            # value of a single coin is the same the coin
            init_layer.append([coin, coin])

        self.next_layer = init_layer

    def calculate_next_layer(self):
        # Function that calculates the next
        # layer of the tree

        # Initialization of the layer
        next_layer = []

        # Iterate over every leaf of the tree layer
        for node in self.next_layer:

            # Iterate over every available coin
            for coin in self.coin_value_list:

                # node[0] contains the previous cash value
                # so we add the coin value in order to find the current one
                current_cash = node[0] + coin

                # list_of_coins contains all the coins added into the sequence
                # for every node of the tree
                list_of_coins = sorted(node[1:] + [coin])

                # if current_cash if larger than self.cash we skip
                # this value because it cant give us a solution anymore
                if current_cash <= self.cash:

                    # We add the current cash value of the
                    # coins to the list
                    check_item = [current_cash] + list_of_coins

                    # If this item is not in the layer we add it
                    if check_item not in self.next_layer:

                        # We add the item into the layer
                        next_layer.append(check_item)

        self.next_layer = next_layer

    def cash_change(self):
        # Function which returns the best
        # solution of the coin problem

        # We start a timer in order to calculate how many time we need in order to run the algorithm
        start = time.time()

        # Maximum depth of the tree
        max_depth = self.cash // min(self.coin_value_list)

        # First layer of the tree
        self.layer_init()

        # Iterate over the maximum possible depth of the tree
        for _ in range(max_depth):

            # Calculate the next layer of the tree
            self.calculate_next_layer()

            # Iterate over every node of the layer and check if we have an answer
            for node in self.next_layer:

                # If we found the answer stop the loop and save it
                # to output, because it is the best solution
                if node[0] == self.cash:
                    self.output = node
                    self.stop = True
                    break

            # Check if we found the best solution
            if self.stop:
                break

        # Print the output and the minimum combinations of coins
        print('The minimum coins required to give change of',
              self.cash, 'are:')

        # Save the combinations of coins only to coins and find the set
        # we use output[1:] because on the output[0] we store the current
        # cash value
        self.coins = sorted(set(self.output[1:]))

        # For every coin we find how many times it was used
        for coin in self.coins:

            print(self.output[1:].count(coin), 'of', coin, '$ value')

        # We end the timer
        end = time.time()

        # If self.timer == True then print the execution time
        if self.timer:

            # We print the time we need to execute the algorithm
            print('\nThe algorithm executed in', "{0:.3f}".format(end - start), 'seconds.')
