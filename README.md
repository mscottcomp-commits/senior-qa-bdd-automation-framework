# Senior QA BDD Automation Framework

## Overview

This project demonstrates a Behavior-Driven Development (BDD) automation framework built using Python, Playwright, and Behave.

The framework uses Gherkin syntax to create business-readable test scenarios and executes them through Playwright automation.

## Tools Used

* Python
* Playwright
* Behave
* Gherkin
* GitHub Actions
* Page Object Model (POM)

## Project Structure

```text
features/
pages/
screenshots/
.github/workflows/
```

## Test Coverage

### Login

* Successful login
* Invalid login validation

### Logout

* Successful logout
* Return to login page validation

## Framework Features

* BDD / Gherkin Scenarios
* Playwright UI Automation
* Page Object Model Design
* Screenshot Capture on Failure
* Reusable Step Definitions
* GitHub Actions CI/CD

## Run Locally

```bash
python -m behave
```

## CI/CD

The framework executes automatically through GitHub Actions on push and pull request events.
