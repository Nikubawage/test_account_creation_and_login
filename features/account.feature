Feature: Account creation and login on Magento

  Scenario: User signs up and logs in successfully
    Given the user launches the browser
    When the user navigates to the home page
    And the user creates a new account
    And the user logs out
    And the user logs in with the same account
    Then the user should see the welcome message
    And the browser is closed