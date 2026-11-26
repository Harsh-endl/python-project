import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("/home/harsh/aiml-project/project/ipl.csv")
decor = {"color":"lightblue",
         "edgecolor":"blue",
         }

def run(df,Name,Runs):
    top = df.nlargest(10,Runs)
    print("\n-------Top 10 batsmen by Runs-------")
    print(top[[Name,Runs]].to_string(index=False))

    top=top.sort_values(by=Runs,ascending = False)
    plt.figure(figsize=(10,6))
    plt.barh(top[Name],top[Runs],**decor)
    plt.title("Top 10 run scorers of 5 years")
    plt.xlabel("Runs")
    plt.ylabel("Players")
    plt.gca().invert_yaxis()
    plt.tight_layout()
    plt.show()

def conc(df,Name,Avg):
    top = df.nlargest(10,Avg)
    print("\n-------Top 10 batsmen by Average-------")
    print(top[[Name,Avg]].to_string(index=False))

    plt.figure(figsize=(10,6))
    top=top.sort_values(by=Avg,ascending = False)
    plt.barh(top[Name],top[Avg],**decor)
    plt.title("Top 10 run scorers of 5 years")
    plt.xlabel("Average")
    plt.ylabel("Players")
    plt.tight_layout()
    plt.gca().invert_yaxis()
    plt.show()

def agg(df,Name,sr):
    top = df.nlargest(10,sr)
    print("\n-------Top 10 batsmen by their strike-rate-------")
    print(top[[Name,sr]].to_string(index=False))

    plt.figure(figsize=(10,6))
    top=top.sort_values(by=sr,ascending = False)
    plt.barh(top[Name],top[sr],**decor)
    plt.title("Top 10 run scorers of 5 years")
    plt.xlabel("Strike rate")
    plt.ylabel("Players")
    plt.tight_layout()
    plt.gca().invert_yaxis()
    plt.show()

def bond(df,Name,six,four):
    df["total"] = df[six]+df[four]
    top = df.nlargest(10,"total")
    print("\n-------Top 10 batsmen by their boundries-------")
    print(top[[Name,six,four]].to_string(index=False))

def indi(df,name):
    print(df.loc[df["Player Name"]==name].to_string(index=False))

def run_per(df,name):
    player = df.loc[df["Player Name"]==name]
    t_six=(player["Sixes"].iloc[0])*6
    t_four=(player["Fours"].iloc[0])*4
    t_run=(player["Total Runs"].iloc[0])-(t_six+t_four)
    contri = np.array([t_run,t_six,t_four])
    slice_label = ["Other runs","Runs from 4s","Runs from 6s"]
    plt.pie(contri,labels=slice_label,
            autopct = "%1.1f%%",
            startangle=90,
            explode=[0.05,0.05,0.05],
            shadow=True,
            colors=["Red","Blue","Yellow"])
    plt.title("Run distribution percentage")
    plt.show()

while(1):
    print("===============CHOICES===============")
    print("Enter 1 for higest run scorers")
    print("Enter 2 for most consistent player")
    print("Enter 3 for aggressive player")
    print("Enter 4 for players with most boundries")
    print("Enter 5 for individual records")
    print("Enter 6 for runs % scored by boundries")
    print("Enter 7 to exit\n")
    print("===============INPUT===============")
    try:
         ip = int(input("Enter your option: "))
    except ValueError:
        print("Try again")
        continue
    if(ip==1):
        run(df,"Player Name","Total Runs")
    elif(ip==2):
        conc(df,"Player Name","Average")
    elif(ip==3):
        agg(df,"Player Name","Strike Rate")
    elif(ip==4):
        bond(df,"Player Name","Sixes","Fours")
    elif(ip==5):
        while(1):
            name = input("Enter player name or 'exit' to exit: ")
            if name in df["Player Name"].values:
                indi(df,name)
                break
            elif name.lower() == "exit":
                break
            else:
                print("Incorrect name!")           
    elif(ip==6):
        while(1):
            name = input("Enter player name or 'exit' to exit: ")
            if name in df["Player Name"].values:
                run_per(df,name)
                break
            elif name.lower() == "exit":
                break
            else:
                print("Incorrect name!")
    elif(ip==7):
        print("Thankyou!")
        break
    else:
        print("Invalid option! Please enter a number from 1 to 7.")

