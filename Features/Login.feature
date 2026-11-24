Feature: Login Feature Testing
  Scenario Outline: Login to the website and verify the dashboard
    Given Open the browser
    When Open the login page
    And Enter the username"<Username>" and password "<Password>"
    Then Verify the dashboad title "<title>"

    |Username    |    Password  | title |
    |prayash888  | prayash@123  | Google|
    |prayash888  | prayash@456  | Google|
