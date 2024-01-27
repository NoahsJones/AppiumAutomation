# Created by noahsj at 12/6/2023
Feature: # Enter feature name here
  # Enter feature description here

  Scenario: Customize explore feed only appears initially.
    Given Click to Skip onboarding
    When Open Customize Explore Feed
    And Go back
    Then Verify CUSTOMIZE ON Explore Feed is not found