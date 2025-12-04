# Created by bjarir at 11/13/2025



Feature: testing reelly.io

  #Scenario 1: off plan page
  Scenario: User can see titles and pictures on each product inside the off plan page

    Given Open the main page
    When  Log in to the login page
    And   Click on “off plan” at the left side menu.
    Then  Verify the right page opens.
    And   Verify each product on this page contains a title and picture visible.
#-----------------------------------------------------------------------------------------------------------------------
  #Scenario 2: Contact us page
  Scenario: User can open the Contact us page
    Given Open the main page
    When  Log in to the login page
    And Clicking on the Setting icon on the left of the page.
    And Click on Contact us tab.
    Then Verify Contact us page opens.
    And Verify that there are at least 4 social media icons.
    And Verify that "connect the company" button is available and clickable.
#-----------------------------------------------------------------------------------------------------------------------
  #Scenario 3: Filter on secondary page
  Scenario: User can filter the secondary deals by "want to sell" option
    Given Open the main page
    When Log in to the login page
    And Click on "Secondary" option at the left side menu
    Then Verify the secondary page opens.
    And Click on filter icon.
    And Click on "want to sell" button.
    And Click on "Apply filter" button.
    And Verify "Listings" and "Agents" exist.
#-----------------------------------------------------------------------------------------------------------------------
  #Scenario 4: the vertical scroll bar button
  Scenario: User can go through the pagination in the secondary page
    Given Open the main page
    When Log in to the login page
    And  Click on "Secondary" option at the left side menu
    And Go to the bottom of the page.
    Then Verify the pagination section at the bottom of the page is visible.
    And  Go back to the top of the page.
    And Verify the grid_menu is visible.
