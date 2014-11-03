##Primitive objective: create all kinds of accounts in financial statements
##Further Objective:
	* able to create current or non current asset total, current or non current liability total, and total of shareholders' equity (stocks and retained earnings)
	* able to create Income statements, which will print all of the following steps
	REVENUE
	- EXPENSE
	---------------------
	Gross Profit
	- SGA EXPENSE
	---------------------
	Operating Income
	- INTERESTS
	- DEPRECIATION, AMORTIZATION
	---------------------
	Pre-tax Income
	- Tax (Pre-tax Income * Statutory Tax Rate)
	----------------------------------------
	Net Income

	* able to create Balance Sheet
	* able to calculate Cash Flow (Operating[O], Investing[I], Financial[F]) _O,I,F will be embedded into instances as an Cash Flow attribute_
	* and able to calculate operating cash flow with indirect methods
	
# Firstly, I need a Swiss knife, which can help me create a new account, and debit or credit money into the account.
In this basis account, the process of book keeping an entry will be as follows:
1, Create an account if it does not exist.
2, debit or credit money into its account.
3, describe what the money goes for	

I call this basis account ACCOUNT, here is a tree structure of its descendant classes

											ACCOUNT
						PERMANENT						  TEMPORARY
  ASSET   LIABILITY   EQUITY   XASSET          REVENUE       EXPENSE
				