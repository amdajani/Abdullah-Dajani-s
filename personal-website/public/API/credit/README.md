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