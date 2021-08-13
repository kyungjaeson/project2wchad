import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

cryptoDF = pd.read_csv('crypto-markets.csv')
#"Test data exists"
# print(cryptoDF.head())
#print(cryptoDF.info())

#convert to datetime
cryptoDF['date'] = pd.to_datetime(cryptoDF['date'], format = "%Y-%m-%d")

#presets

oldest_cryptoDF = pd.DataFrame({'start_date':cryptoDF.groupby(["name"])['date'].min()}).reset_index()

#functions
def oldest_crypto_finder(num):
    print(oldest_cryptoDF.sort_values(['start_date']).head(num))

def newest_crypto_finder(num):
    print(oldest_cryptoDF.sort_values(['start_date']).tail(num))

def crypto_grapher(num):
    axis = cryptoDF.groupby(['name'])['market'].last().sort_values(ascending=False).head(num).sort_values().plot(
        kind='barh')
    axis.set_xlabel("Market cap (USD) in Billions")
    plt.title(f"Top {num} Currencies by Market")
    plt.savefig(f"output{num}.png")
    print("Printed your graph")


#prompter


while True:
    answer = input(
        """
Learn more about crypto
What do you want to find out: 
A. Oldest crypto
B. Newest crypto
C. Generate a plot of top crypto

type A,B, C:

        """)
    if answer == 'A':
        numerical_input = input("How many?")
        print("Oldest crypto list")
        oldest_crypto_finder(int(numerical_input))
    elif answer == 'B':
        numerical_input = input("How many?")
        print("Newest crypto list")
        newest_crypto_finder(int(numerical_input))
    elif answer == 'C':
        numerical_input = input("How many?")
        crypto_grapher(int(numerical_input))

    else:
        print("I dont know what that is")



