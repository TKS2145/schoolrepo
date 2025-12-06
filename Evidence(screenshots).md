# schoolrepo

This is the file which I  will be using to share screenshots of my program and write my self reflection on.

I am running the program from my linux command line directly as it provides better readability than the visual studio code command line

Here is the start:

![alt text](https://github.com/TKS2145/schoolrepo/tree/main/Screenshots/Screenshot_20251205_233327.png)

As can be seen, the program works and an option screen (on command line) is displayed. 
Atempting to list transactions before adding any transactions returns the above message that there is nothing to list as all is empty.
Program does not crash and option screen is displayed again awaiting for user to do the needfull.

![alt text](Screenshot_20251205_233548.png)

Trying to filter when no transactions were added also gives the same result and option screen is displayed again.

![alt text](Screenshot_20251205_233833.png)

Same for summary. Program does not crash when all data are empty.

![alt text](Screenshot_20251205_234223.png)

Here is just to show that the program exits wll even giving a goodbye message. I feel I should get these little details out of the way before diving into the deeper parts.

![alt text](Screenshot_20251205_234336.png)

Here a new transaction of type income has been added. Data is in float type allowing decimals to be entered.


![alt text](Screenshot_20251205_234617.png)

List module works as seen above. Skiping expense as it uses the same functionalities.

![alt text](Screenshot_20251206_000901.png)

Expense is also added without issue

![alt text](Screenshot_20251206_001415.png) 
![alt text](Screenshot_20251206_001425.png)

Added more incomes and expenses

![alt text](Screenshot_20251206_001629.png)

As can be seen, the list module to list the transactions works
Incomes and Expenses are listed separately allowing easy redability

![alt text](Screenshot_20251206_001809.png)

Entering a number outside 5 does not crash the program, user is asked to enter the number again and entering a text does not crash and a slightly different message is sent to the user

![alt text](Screenshot_20251206_002221.png)

Summary also works and provides number of incomes, number of expenses, sum of all incomes, sum of all expenses and provides the amount saved.


Using different data to test if expenses is greater than income:

![alt text](Screenshot_20251206_010648.png)

As seen, when expense is greater than income, the amount due is shown instead and here it is 1000
I deliberately did not add a unit (Roupies nor Dollars). That way the user can calculate using any currency he/she wants

![alt text](Screenshot_20251206_011017.png)

Rare case total incomes and total expenses are exactly the same, messages changes to reflect all money spent.


![alt text](Screenshot_20251206_011437.png)

Confirming option 3 to list transaction works

![alt text](Screenshot_20251206_115340.png)

Here is the new data and the filter menu allowing 3 possible ways to filter the data.


![alt text](Screenshot_20251206_120748.png)

When categoryy is selected, all different categorices are obtained and displayed. The user has to enter the number corresponding to the category he/she wishes to filter by. This prevent user typos.

![alt text](image.png)
 
 As seen here, there is 'Gift' catogory twice, one in income and one in expense. Still, 'Gift' catogory appears only once in the category list.

 ![alt text](image-1.png)

 As seen here, it does not fail to display all transactions which have a 'Gift' category.

 ![alt text](Screenshot_20251206_122313.png)

 ![alt text](Screenshot_20251206_122447.png)

 Here we can see that the filtering by month works perfectly.

![alt text](Screenshot_20251206_122615.png)

And here lastly is the filter by type. Since the 'filter by type' does the same thing as 'list transaction' module, I used modular programing to reuse existing module.

Last test:

![alt text](Screenshot_20251206_123824.png)

As seen 'TESING' category was entered but the Category is captitalised to make it consistent and remove lower/upper case issues.


Lastly:

![alt text](Screenshot_20251206_122830.png)

Showing a summary and finish the program. All works fine and the program is safe from  user crashing it. It also accounts for several user misteps but since it is customisable for thee user , user enters its own categories, typos can make it a little messy for the user but the program will not crash.

Thank you for reading and going through this README file
