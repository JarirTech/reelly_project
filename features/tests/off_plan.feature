# Created by bjarir at 11/13/2025



Feature: testing reelly.io


  Scenario: User can see titles and pictures on each product inside the off plan page

    # Enter steps here
    Given Open the main page
    When  Log in to the login page
    And   Click on “off plan” at the left side menu.
    Then  Verify the right page opens.
    And   Verify each product on this page contains a title and picture visible.


  Scenario: User can open the Contact us page
    Given Open the main page
    When  Log in to the login page
    And Clicking on the Setting icon on the left of the page.
    And Click on Contact us tab.
    Then Verify Contact us page opens.
    And Verify that there are at least 4 social media icons.
    And Verify that "connect the company" button is available and clickable.
