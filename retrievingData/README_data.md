# StockTrader
Inside the folder "retrievingData", there are broadly two types of .csv files: those that are raw data (price, weather, volumes, etc.), and those that are data from our agents.

Raw Data: (which was generally run via the python file "get_data.py" BEWARE SAVING TO THE SAME FILE NAME)


DO_NOT_USE_first_data.csv -- this file is from Monday December 3rd, 11:15am, and it only lasted about an hour and a half. Note that this file has price info only from FB, MSFT, AMZN, and AAPL. This also contains weather info. Note that there was some kind of error in which it didn't record points for a few minutes. DO NOT USE THIS FILE becuase it only has 4 stocks present

second_data.csv -- this file is from Monday, December 10th, 10:06am, and it ran until about 3pm that day (with data from about every single minute). This also includes additional price info, from the 4 before but also from SHAK, WEN, NFLX, TSLA, MCD. This data is preferred for data testing

third_data.csv -- this file is from Thursday, December 13th, 10:02am, ran until about 3pm that day. Same info from second_data (i.e. same price info and same weather info)

fourth_data.csv -- this file is from Friday, December 14th, 10:00am to about 3pm. Same info as previous 2 raw files

Agent data:

In the folder approxAgentData

Approximate Q - Learning agent (uses approxAgent.py)

In oldData
-fixed_approx_just_apple_just_derivative.csv --> an agent that only BUYs or SELLs a single share of apple, using the feature that is just the derivative. Note that "base case" is an agent that starts out with the same materials, but never BUYs or SELLs.

-fixed_approx_all_stocks_just_derivative.csv --> agent that only BUYs or SELLs a single share of apple, microsoft, amazon, facebook, using only the derivative as a feature.
 
-second_data_all_stocks_with_bostemp_boshumid_MACDSMAdiffsimplederiv.csv --> note that the weights blew right up, and the graph is pretty bad. This is good to show as a proof that certain things didn't matter

-   second_data_all_stocks_with_bostemp_MACDSMAdiffsimplederiv.csv
this file is successful, but overall weather shouldn't be trusted. This just used boston temperature, and the weight is below 62046906.7691

    In approxGoodData
        
    - each file is titled with which dataset it's from (second, third, or 4th). All three use all 9 stocks, all three use the 3 intresting numbers (MACD, SMA difference, and simple derivative). Overall, we had very good success in 2nd and 3rd, and the 4th was good until the end when it completely tanks
    - the weights corresponding to a (symbol, key) pair are also there
    
    
In the folder regressionAgentData

This is the agent that uses regression to predict if the price is going up or down

In regressionGoodData, there are 6 files, 3 for linear and 3 for poly. The linear files correspond to an agent that looks at n=10 past prices and uses linear regression to predict the slope, and then buys if the slope is going down (i.e. with the hope that it will then go up) and sells if the slope is going up. Poly uses n=20 past prices with a degree m=7 polynomial, uses the derivative at zero at determine the "slope", and uses the same reasoning from linear. As one might expect, this m=7 degree polynomial is not very reliable, but it often does make good money in these 3 test cases









