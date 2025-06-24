import pyautogui, time
from rich import print
part2 = r"""
                                                           
,--.   ,--. ,-----. ,--.  ,--.,--. ,--.,------.,--.   ,--. 
|   `.'   |'  .-.  '|  ,'.|  ||  .'   /|  .---' \  `.'  /  
|  |'.'|  ||  | |  ||  |' '  ||  .   ' |  `--,   '.    /   
|  |   |  |'  '-'  '|  | `   ||  |\   \|  `---.    |  |    
`--'   `--' `-----' `--'  `--'`--' '--'`------'    `--'    
,--------.,--.   ,--.,------. ,------.                     
'--.  .--' \  `.'  / |  .--. '|  .---'                     
   |  |     '.    /  |  '--' ||  `--,                      
   |  |       |  |   |  | --' |  `---.                     
   `--'       `--'   `--'     `------'          
"""
q = "Hi from cheat for monkey type!"
print(f"[bold violet]{part2}[/bold violet]")
print(f"[bold violet]{q}[/bold violet]")
YorN = input("Do you want activate(y/n):")
yes = "y"
no = "n"
if YorN == yes:
    dire = input("Path TXT words:")
    activ = "Activated, wait 5 sec..."
    print(f"[bold green]{activ}[/bold green]")
    time.sleep(5); f = open(dire, "r")
    for line in f:
        pyautogui.typewrite(line)
if YorN == no:
    ok = "Ok"
    print(f"[bold yellow]{ok}[/bold yellow]")
else:
    incor = "Incorrect command"
    print(f"[bold red]{incor}[/bold red]")
