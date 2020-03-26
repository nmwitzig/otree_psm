# <imports>
from otree.api import Currency as c
from otree.constants import BaseConstants
# </imports>


# ******************************************************************************************************************** #
# *** CLASS CONSTANTS *** #
# ******************************************************************************************************************** #
class Constants(BaseConstants):

    # ---------------------------------------------------------------------------------------------------------------- #
    # --- Task-specific Settings --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    # lottery payoffs
    # "high" and "low" outcomes (in currency units set in settings.py) of the Lottery option
    # "safe_payment" denotes the initial safe payment, i.e. safe payment at row 1
    # "increment" determines how much the safe payment increases at each row

    lottery_hi = 300
    lottery_lo = 0
    safe_payment = 0
    increment = 10

    # currency format
    currency = 'Euro'

    # number of binary choices between "lottery" and "safe payment"
    num_choices = 31

    # include 'certain' choice
    certain_choice = True

    # ---------------------------------------------------------------------------------------------------------------- #
    # --- Overall Settings and Appearance --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    # show each lottery pair on a separate page
    # if <one_choice_per_page = True>, each single binary choice is shown on a separate page
    # if <one_choice_per_page = False>, all <num_choices> choices are displayed in a table on one page
    one_choice_per_page = False

    # order choices between lottery pairs randomly
    # if <random_order = True>, the ordering of binary decisions is randomized for display
    # if <random_order = False>, binary choices are listed in ascending order of the probability of the "high" outcome
    random_order = False

    # enforce consistency, i.e. only allow for a single switching point
    # if <enforce_consistency = True>, all options "A" above a selected option "A" are automatically selected
    # similarly, all options "B" below a selected option "B" are automatically checked, implying consistent choices
    # note that <enforce_consistency> is only implemented if <one_choice_per_page = False> and <random_order = False>
    enforce_consistency = True

    # depict probabilities as percentage numbers
    # if <percentage = True>, the probability of outcome "high" will be displayed as percentage number, i.e. "50%"
    # if <percentage = False>, the probabilities will be displayed as fractions, i.e. "1/2" etc.
    percentage = True

    # show small pie charts for each lottery
    # if <small_pies = True>, a pie chart depicting the probabilities of outcomes is rendered next to each lottery
    # if <small_pies = False>, no graphical representation of probabilities is displayed
    small_pies = True

    # display lotteries in terms of large pie charts
    # if <large_pies = True>, lotteries are depicted as pie charts; if <large_pies = False> lotteries are list items
    # note that <large_pies = True> only affects the task's appearance if <one_choice_per_page = True>
    large_pies = True

    # show progress bar
    # if <progress_bar = True> and <one_choice_per_page = True>, a progress bar is rendered
    # if <progress_bar = False>, no information with respect to the advance within the task is displayed
    # the progress bar graphically depicts the advance within the task in terms of how many decision have been made
    # further, information in terms of "page x out of <num_choices>" (with x denoting the current choice) is provided
    progress_bar = True

    # show instructions page
    # if <instructions = True>, a separate template "Instructions.html" is rendered prior to the task
    # if <instructions = False>, the task starts immediately (e.g. in case of printed instructions)
    instructions = True

    # show results page summarizing the task's outcome including payoff information
    # if <results = True>, a separate page containing all relevant information is displayed after finishing the task
    # if <results = False>, the template "Results.html" will not be rendered
    results = False

    # null payoff (if results is false and the task is not incentive compatible)
    null_payoff = 0

    # ---------------------------------------------------------------------------------------------------------------- #
    # --- oTree Settings (Don't Modify) --- #
    # ---------------------------------------------------------------------------------------------------------------- #

    name_in_url = 'mpl'
    players_per_group = None

    if one_choice_per_page:
        if certain_choice:
            num_rounds = num_choices
        else:
            num_rounds = num_choices - 1
    else:
        num_rounds = 1
