/*# Credit-Card-Check-Using-Luhn-s-Algorithm
This code is designed to receive an input from the user for a credit card number.
Then it will run a checksum using Luhn's algorithm. If the credit card is not valid,
the output will be as such, else if it is valid, the code will then determine
the type of credit card (VISA, MASTERCARD, AMEX).*/

#include <cs50.h>
#include <math.h>
#include <stdio.h>

int everyOtherNumber(long creditCard);
int getSum2Digits(int x);
int getDigits(long creditCard);
bool isValidAMEX(long creditCard, int digitNum);
bool isValidVISA(long creditCard, int digitNum);
bool isValidMASTER(long creditCard, int digitNum);

int main()
{
    // prompts the user for input and stores it as a long format
    long creditCard = get_long("Number: ");
    // calls the function everyOtherNumber
    int everyOther = everyOtherNumber(creditCard);
    // calls the function getDigits
    int digitNum = getDigits(creditCard);
    // checks AMEX
    bool AMEX = isValidAMEX(creditCard, digitNum);
    // checks VISA
    bool VISA = isValidVISA(creditCard, digitNum);
    // checks MasterCard
    bool MASTER = isValidMASTER(creditCard, digitNum);

    if (everyOther % 10 != 0)
    {
        printf("INVALID\n");
        return 0;
    }
    else if (AMEX == true)
    {
        printf("AMEX\n");
    }
    else if (VISA == true)
    {
        printf("VISA\n");
    }
    else if (MASTER == true)
    {
        printf("MASTERCARD\n");
    }
    else
    {
        printf("INVALID\n");
    }
}

// First user-defined function
int everyOtherNumber(long creditCard)
{
    int sum = 0;
    bool IsAlternateDigit = false;
    while (creditCard > 0)
    {
        if (IsAlternateDigit == true)
        {
            int lastDigit = creditCard % 10;
            int product = getSum2Digits(lastDigit);
            sum += product;
        }
        else
        {
            int lastDigit = creditCard % 10;
            sum += lastDigit;
        }
        IsAlternateDigit = !IsAlternateDigit;
        creditCard /= 10;
    }
    return sum;
}

int getSum2Digits(int lastDigit)
{
    int multiply = lastDigit * 2;
    int sum = 0;
    while (multiply > 0)
    {
        int lastDigitMultiply = multiply % 10;
        sum += lastDigitMultiply;
        multiply /= 10;
    }
    return sum;
}

int getDigits(long creditCard)
{
    int digits;
    long creditCardNum = creditCard;
    for (digits = 0; creditCardNum > 0; digits++)
    {
        creditCardNum /= 10;
    }
    return digits;
}
bool isValidAMEX(long creditCard, int digitNum)
{
    int firstTwoDigits = creditCard / pow(10, (13));

    if ((digitNum == 15) && (firstTwoDigits == 34 || firstTwoDigits == 37))
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool isValidVISA(long creditCard, int digitNum)
{
    int firstTwoDigits1 = creditCard / pow(10, 12);
    int firstTwoDigits2 = creditCard / pow(10, 15);

    if ((digitNum == 13) && (firstTwoDigits1 == 4))
    {
        return true;
    }
    else if ((digitNum == 16) && firstTwoDigits2 == 4)
    {
        return true;
    }
    else
    {
        return false;
    }
}

bool isValidMASTER(long creditCard, int digitNum)
{
    int firstTwoDigits = creditCard / pow(10, (14));

    if ((digitNum == 16) && (firstTwoDigits >= 51 && firstTwoDigits <= 55))
    {
        return true;
    }
    else
    {
        return false;
    }
}
