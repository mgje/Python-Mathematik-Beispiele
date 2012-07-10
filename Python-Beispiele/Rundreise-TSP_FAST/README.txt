
Die Simulation kann mit der folgenden Kommandozeile gestartet werden.

Mit Simulated Anealing
python tsp.py -o out.png -a anneal --cooling 10.0:0.9998 -n 40000 city100.txt 


python tsp.py -o out.png -a hillclimb -n 40000 city100.txt 



Parameter:
python tsp.py [-o <output image file>] [-v] [-m reversed_sections|swapped_cities] -n <max iterations> [-a hillclimb|anneal] [--cooling start_temp:alpha] <city file>