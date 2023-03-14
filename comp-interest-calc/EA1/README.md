# First stage of the project

For this step we will develop a compound interest calculator. The difficulty here was choosing a project that had some real utility and that fit the restriction of a maximum of 20 steps for the flowchart.

The calculator will ask the user to input 4 variables: initial amount, monthly contribution, investment time and the expected interest rate. With these variables in memory, we will use a "FOR" looping structure. This structure will iterate from zero to the total years of the investment. And, at each iteration, it will calculate the gain value for that year and add it to previous years. Inside the loop we will also use a conditional structure to check if the final result is zero and, if so, assign the initial deposit amount to it. This condition is intended to assign the initial deposit amount to the final amount in the first iteration. Upon completion of the loop, we will show the user how much it would have potentially accumulated over those years.
