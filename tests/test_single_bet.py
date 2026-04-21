import pytest 
from pages.single_bet_page import SingleBetPage
from conftest import driver


"""
Placing  a single bet on the home team with odds of 2.45 and verifying that the bet is placed successfully.
"""

def test_place_single_bet(driver):
    single_bet_page = SingleBetPage(driver)
    single_bet_page.odds_selection()
    single_bet_page.enter_stake_amount()
    single_bet_page.place_bet()
    single_bet_page.verify_bet_placement()
    
