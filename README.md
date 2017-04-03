# BotWRouter
This is a toolkit that allows you to route out various BotW categories using a weighted TSP algorithm.  
It currently uses height differences and warps to hopefully speedup the route.  

## Key  
Red dots: Shrines  
Green dots: Koroks  
Transparent line: warp  
Solid line: Overworld movement  

## Data
The locations were extracted from the game, and contain the X, Y, and Z coordinates of the koroks and shrines.

## Usage  
First, install the requirements `pip install -r requirements.txt`  
Then, run the script for the category you want`python shrines.py` or `python hundo.py`
