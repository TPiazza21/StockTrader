# StockTrader
Inside the folder "retrievingData", there are broadly two types of .csv files: those that are raw data (price, weather, volumes, etc.), and those that are data from our agents.

Raw Data: (which was generally run via the python file "get_data.py" BEWARE SAVING TO THE SAME FILE NAME)


first_data.csv -- this file is from Monday December 3rd, 11:15am, and it only lasted about an hour and a half. Note that this file has price info only from FB, MSFT, AMZN, and AAPL. This also contains weather info. Note that there was some kind of error in which it didn't record points for a few minutes

second_data.csv -- this file is from Monday, December 10th, 10:06am, and it ran until about 3pm that day (with data from about every single minute). This also includes additional price info, from the 4 before but also from SHAK, WEN, NFLX, TSLA, MCD. This data is preferred for data testing

third_data.csv -- this file is from Thursday, December 13th, 10:02am, ran until about 3pm that day. Same info from second_data (i.e. same price info and same weather info)

fourth_data.csv -- this file is from Friday, December 14th, 10:00am to about 3pm. Same info as previous 2 raw files

Agent data:

FROM FIRST_DATA.CSV (i.e. the agent runs, as if it was the same time as first_data.csv)

Approximate Q - Learning agent (uses approxAgent.py)

-fixed_approx_just_apple_just_derivative.csv --> an agent that only BUYs or SELLs a single share of apple, using the feature that is just the derivative. Note that "base case" is an agent that starts out with the same materials, but never BUYs or SELLs.

-fixed_approx_all_stocks_just_derivative.csv --> agent that only BUYs or SELLs a single share of apple, microsoft, amazon, facebook, using only the derivative as a feature.









