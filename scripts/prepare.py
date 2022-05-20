import os
import json
import pandas as pd
import matplotlib.pyplot as plt

inputdir = './output'
outputdir = './img'
result = {}
for filename in os.listdir(inputdir):
    fp = os.path.join(inputdir, filename);
    if os.path.isfile(fp):
        fnameparts = filename.replace('-', '.').split('.');
        name = fnameparts[0];
        df = pd.read_csv(fp, parse_dates=['SOLD DATE MONTH'])
        grouped = df.groupby('SOLD DATE MONTH').agg({'$/SQUARE FEET Adjusted': ['median', 'count']});
        v = grouped.values;
        result[name] = {
            'x': list(grouped.index.astype(str)),
            'series': [list(v[:,0]),list(v[:,1])]
        };

with open('../charts.json', 'w') as fp:
    json.dump(result, fp)
