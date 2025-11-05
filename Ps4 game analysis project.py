import pandas as pd
import matplotlib.pyplot as plt

game_data = pd.read_csv(r"C:\Users\admin\Documents\GameData.csv")
game_data.set_index("Games", inplace=True)
game_data["Games"] = game_data.index 

while True:
    print("\nMain Menu")
    print("1. Display the DataFrame")
    print("2. DataFrame Statistics")
    print("3. Display Records")
    print("4. Working on Columns")
    print("5. Search Specific Row/Column")
    print("6. Data Visualization")
    print("7. Exit")

    try:
        ch = int(input("Enter your Choice: "))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 7.")
        continue

    if ch == 1:
        print(game_data)

    elif ch == 2:
        while True:
            print("\nDataFrame Statistics Menu")
            print("1. Display the Transpose")
            print("2. Display all Column Names")
            print("3. Display the indexes")
            print("4. Display the Shape")
            print("5. Display the Dimension")
            print("6. Display the Data types of all Columns")
            print("7. Display the Size")
            print("8. Exit")

            try:
                ch2 = int(input("Enter Your Choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if ch2 == 1:
                print(game_data.T)
            elif ch2 == 2:
                print(game_data.columns)
            elif ch2 == 3:
                print(game_data.index)
            elif ch2 == 4:
                print(game_data.shape)
            elif ch2 == 5:
                print(game_data.ndim)
            elif ch2 == 6:
                print(game_data.dtypes)
            elif ch2 == 7:
                print(game_data.size)
            elif ch2 == 8:
                break

    elif ch == 3:
        while True:
            print("\nDisplay Records Menu")
            print("1. Top 5 Records")
            print("2. Bottom 5 Records")
            print("3. Specific number of records from the top")
            print("4. Specific number of records from the bottom")
            print("5. Exit")

            try:
                ch3 = int(input("Enter Your Choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if ch3 == 1:
                print(game_data.head())
            elif ch3 == 2:
                print(game_data.tail())
            elif ch3 == 3:
                try:
                    n = int(input("Enter how many records do you want from the top: "))
                    print(game_data.head(n))
                except ValueError:
                    print("Please enter a valid number.")
            elif ch3 == 4:
                try:
                    n = int(input("Enter how many records do you want from the bottom: "))
                    print(game_data.tail(n))
                except ValueError:
                    print("Please enter a valid number.")
            elif ch3 == 5:
                break

    elif ch == 4:
        while True:
            print("\nWorking on Columns Menu")
            print("1. Insert a new column data")
            print("2. Delete a specific column")
            print("3. Exit")

            try:
                ch4 = int(input("Enter your Choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if ch4 == 1:
                h = input("Enter column/heading name: ")
                try:
                    det = eval(input("Enter Details (enclosed in []): "))
                    game_data[h] = pd.Series(data=det, index=game_data.index)
                    print("Column inserted")
                except Exception as e:
                    print(f"Error: {e}")
            elif ch4 == 2:
                a = input("Enter column name to be Deleted: ")
                if a in game_data.columns:
                    game_data.drop(columns=[a], inplace=False)
                    print("Column Temporarily Deleted")
                else:
                    print("Column not found.")
            elif ch4 == 3:
                break

    elif ch == 5:
        while True:
            print("\nSearch Menu")
            print("1. Search for the details of a specific row by index")
            print("2. Search details of a specific column")
            print("3. Exit")

            try:
                ch5 = int(input("Enter your Choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if ch5 == 1:
                st = input("Enter the index of the row you want to see: ")
                if st in game_data.index:
                    print(game_data.loc[st])
                else:
                    print("Row not found.")
            elif ch5 == 2:
                col = input("Enter column/heading name whose details you want to see: ")
                if col in game_data.columns:
                    print(game_data[col])
                else:
                    print("Column not found.")
            elif ch5 == 3:
                break

    elif ch == 6:
        while True:
            print("\nData Visualization")
            print("1. Line Chart")
            print("2. Vertical Bar Plot")
            print("3. Horizontal Bar Plot")
            print("4. Exit")

            try:
                ch6 = int(input("Enter your Choice: "))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
                continue

            if ch6 == 1:
                plt.figure(figsize=(12, 8))
                plt.plot(game_data.index, game_data['Price'], 'g-o', label='Price')
                plt.xlabel("Games")
                plt.ylabel("Price")
                plt.title("Line Chart of Price")
                plt.legend()
                plt.xticks(rotation=45)
                plt.grid(True)
                plt.tight_layout()
                plt.show()

                plt.figure(figsize=(14, 8))
                plt.plot(game_data.index, game_data['Lifetime Sales'], 'b-o', label='Lifetime Sales', markersize=8, linewidth=2)
                plt.xlabel("Games", fontsize=12)
                plt.ylabel("Lifetime Sales (in units)", fontsize=12)
                plt.title("Lifetime Sales Line Chart", fontsize=16)
                plt.xticks(rotation=45)
                plt.grid(True, linestyle='--', alpha=0.7)
                plt.tight_layout()
                plt.show()

            elif ch6 == 2:
                game_data['Price'].plot(kind='bar', figsize=(10, 6), color='green')
                plt.title("Vertical Bar Chart of Prices")
                plt.xlabel("Games")
                plt.ylabel("Price")
                plt.xticks(rotation=45)
                plt.show()

                game_data['Lifetime Sales'].plot(kind='bar', figsize=(10, 6), color='blue')
                plt.title("Vertical Bar Chart of Lifetime Sales")
                plt.xlabel("Games")
                plt.ylabel("Lifetime Sales")
                plt.xticks(rotation=45)
                plt.show()

            elif ch6 == 3:
                game_data['Price'].plot(kind='barh', figsize=(10, 6), color='green')
                plt.title("Horizontal Bar Chart of Prices")
                plt.xlabel("Price")
                plt.ylabel("Games")
                plt.show()

                game_data['Lifetime Sales'].plot(kind='barh', figsize=(10, 6), color='blue')
                plt.title("Horizontal Bar Chart of Lifetime Sales")
                plt.xlabel("Lifetime Sales")
                plt.ylabel("Games")
                plt.show()

            elif ch6 == 4:
                break

    elif ch == 7:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid Choice. Please enter a number between 1 and 7.")




