# Created by bjarir at 11/13/2025



Feature: testing off plan page


  Scenario: User can see titles and pictures on each product inside the off plan page

    # Enter steps here
    Given Open the main page
    When  Log in to the login page
    And   Click on “off plan” at the left side menu.
    Then  Verify the right page opens.
    And   Verify each product on this page contains a title and picture visible.
