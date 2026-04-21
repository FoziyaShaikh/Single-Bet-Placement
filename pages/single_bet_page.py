import pytest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.settings import DEFAULT_WAIT, LONG_WAIT

class SingleBetPage:
    def __init__(self, driver):
        self.driver = driver

        # --- Locators for the elements to place a bet ---
        self.select_odds = (By.XPATH, "//button//span[contains(text(),'2.45')]")
        self.stake_input = (By.XPATH, "//input[@id='bet-slip-stake-input']")
        self.place_bet_button = (By.XPATH, "//button[contains(text(),'Place Bet')]")
       
        #--- Locators for the elements to verify bet placement ---
        self.title = (By.XPATH, "//h2[contains(text(),'Bet Placed Successfully!')]")
        self.stake = (By.XPATH, "//div[@id='modal-success-stake']")
        self.odds = (By.XPATH, "//div[@id='modal-success-odds']")



    # --- Actions for interacting with the elements on the single bet page ---
    def odds_selection(self):
        WebDriverWait(self.driver,DEFAULT_WAIT).until(EC.element_to_be_clickable(self.select_odds)).click()

    def enter_stake_amount(self):
        WebDriverWait(self.driver,DEFAULT_WAIT).until(EC.element_to_be_clickable(self.stake_input)).send_keys("1")

    def place_bet(self):
        WebDriverWait(self.driver,DEFAULT_WAIT).until(EC.element_to_be_clickable(self.place_bet_button)).click()

    #Function to verify that the bet is placed successfully by checking for the presence of a confirmation message and validating the displayed odds and stake amount.
    def verify_bet_placement(self):
        assert WebDriverWait(self.driver, LONG_WAIT).until(EC.visibility_of_element_located(self.title)).is_displayed(), "Bet placement confirmation message is not displayed."
        assert WebDriverWait(self.driver, LONG_WAIT).until(EC.visibility_of_element_located(self.stake)).text == "€1.00", f"Expected stake amount to be '1', but got '{self.stake.text}'."
        assert WebDriverWait(self.driver, LONG_WAIT).until(EC.visibility_of_element_located(self.odds)).text == "2.45", f"Expected odds to be '2.45', but got '{self.odds.text}'."
    
    # If the bet is placed successfully, the test will pass. If any of the assertions fail, an AssertionError will be raised with a message indicating the reason for the failure.
        print("Test passed: Bet placed successfully with the correct odds and stake amount.")

  