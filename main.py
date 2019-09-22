# Dependencies
import CoinClass
import utils


# Main function of our program
if __name__ == '__main__':

    # Load of the Configuration file
    conf = utils.parse_yaml('conf.yaml')

    # Class initializer and function run
    min_coin = CoinClass.CoinProblem(cfg=conf)
    min_coin.cash_change()

