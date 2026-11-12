@login
Feature: Login functionality
  As a registered user
  I want to log in with my credentials
  So that I can see my dashboard

  Scenario Outline: Successful login shows the dashboard
    Given the user is on the login page
    When the user logs in with username "<username>" and password "<password>"
    Then a screenshot of the page after login is captured
    And the dashboard title "<title>" should be visible
    And the username "<username>" should be displayed on the dashboard

    Examples:
      | username | password     | title     |
      | prayash  | prayash@123  | Dashboard |
      | Sahoo    | Sahoo@123    | Dashboard |
