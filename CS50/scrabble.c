#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <string.h>

#define NUMPLAYER 2

// get intputs from user as an array
void getInput(string word[NUMPLAYER]);

// UDF to calcualte how much points word 1 and 2 got
void calcScore(string word[NUMPLAYER], int score[NUMPLAYER]);

// sorting algorithm to determine the max number in the array and for
// whom it belongs to
void sortingScore(int score[NUMPLAYER], int playerIndex[NUMPLAYER]);

// simply checks winner/tie
void displayOutput(int score[NUMPLAYER], int playerIndex[NUMPLAYER]);

int main(void)
{

    string playerWord[NUMPLAYER]; // initializing an array of two string places
    getInput(playerWord);         // calling the input function

    int playerScore[NUMPLAYER] = {0};   // initializing a score array
    calcScore(playerWord, playerScore); // calling to calculating the total points for players

    int playerIndex[NUMPLAYER];
    for (int i = 0; i < NUMPLAYER; i++)
    {
        playerIndex[i] = i; // Initializes each player's index
    }
    sortingScore(playerScore,
                 playerIndex); // calling to implement a sorting algorithm (Bubble Sort)

    displayOutput(playerIndex, playerScore); // checks Ties/Winners and displays it.
}

// UDF for input
void getInput(string word[NUMPLAYER])
{
    for (int i = 0; i < NUMPLAYER; i++)
    {
        word[i] = get_string("Player %d: ", i + 1);
    }
}

// UDF for score calculation
void calcScore(string word[NUMPLAYER], int score[NUMPLAYER])
{
    // This is the value of each letter in scrabble, ordered.
    int letterScore[26] = {1, 3, 3, 2,  1, 4, 2, 4, 1, 8, 5, 1, 3,
                           1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

    for (int i = 0; i < NUMPLAYER; i++)
    {
        for (int j = 0; word[i][j] != '\0'; j++)
        {
            char letter = toupper(word[i][j]); // initializing the and capitalizing the letter
            if (letter >= 'A' && letter <= 'Z')
            {
                int letterIndex = letter - 'A';
                score[i] += letterScore[letterIndex];
            }
            else
            {
                continue;
            }
        }
    }
}

// UDF for sorting score
void sortingScore(int score[NUMPLAYER], int playerIndex[NUMPLAYER])
{
    // Bubble Sort algorithm implemented
    for (int i = 0; i < NUMPLAYER - 1; i++)
    {
        for (int j = 0; j < NUMPLAYER - i - 1; j++)
        {
            if (score[j] < score[j + 1])
            {
                int swapScore = score[j];
                score[j] = score[j + 1];
                score[j + 1] = swapScore;

                int swapIndex = playerIndex[j];
                playerIndex[j] = playerIndex[j + 1];
                playerIndex[j + 1] = swapIndex;
            }
        }
    }
}

// UDF for checking and displaying winner
void displayOutput(int playerIndex[NUMPLAYER], int score[NUMPLAYER])
{
    if (score[0] == score[1])
    {
        printf("It's a tie!\n");
    }
    else
    {
        printf("Player %d wins!\n", playerIndex[0] + 1);
    }
}
