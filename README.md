#TKS's README

Here is my Budgect tracker assignment which will count as my first formative for programing 1.

The project fully command line and has several file which work together.

To run the program, the file "BudgectTracker.py" must be run (either from an IDE or terminal). It contains the main of the program and calls every file which is needed when needed.

The project will start and ask the user to press enter to start, then a sample Menu will be displace giving the option to choose between  6 options:
Adding income, adding expenses, list transactions, filter the data, show a summary or exit the program.

The user has to follow what the program ask of him/her.

The program has several exception handling in it so it is nearly impossible for a normal user to crash it. 

It also accounts for user trying to list data before inputing the data.

The menu is iterative so once an option has finished processing, the program waits for the user to press 'enter' then displays the menu again.
The program exits when the user chooses '0' as option and displays a short closing message.

Modular programing is used a lot allowing code reusability.

Sample Interaction:

    User runs BudgetTracker.py
    Progams ask user to press enter
    User presses enter and menu is displayed

    User presses 1 and 2 to enter income and expense respectively.
    User enters the data.

    User can press 3 to list transactions and get a short view of the transactions entered.
    User can choose to filter by choosing option 4
    User chooses 5 to be shown a summary and how much money user is saving or owing.

    User chooses option 0 to exit the program
    Closing message is displayed

If you need more detail, please go through [text](Evidence(screenshots).md) for most possible interactions.

