# Abdullah Dajani's Projects

Welcome to my project repository! Here you'll find a collection of my work, showcasing my skills in software development, web design, and more.


Feel free to explore the projects and reach out if you have any questions or collaboration ideas.


# Credit Card Validation API

## Description
This API allows users to validate credit card numbers and determine their type.

## Endpoints

### Validate Credit Card

- **URL**: `/credit-cards`
- **Method**: `POST`
- **Request Body**:
  - `credit_card`: The credit card number to validate (integer)

- **Response**:
  - `status`: `success` or `error`
  - `message`: Information about the validation result
  - `type`: The type of the credit card if valid (e.g., `VISA`, `MASTERCARD`, `AMEX`)