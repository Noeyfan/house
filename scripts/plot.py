import os
import pandas as pd
import matplotlib.pyplot as plt

inputdir = './output'
outputdir = './img'
for filename in os.listdir(inputdir):
    fp = os.path.join(inputdir, filename);
    if os.path.isfile(fp):
        fnameparts = filename.replace('-', '.').split('.');
        name = fnameparts[0];
        df = pd.read_csv(fp, parse_dates=['SOLD DATE MONTH'])
        grouped = df.groupby('SOLD DATE MONTH').agg({'$/SQUARE FEET Adjusted': ['median', 'count']});
        grouped.plot(xlabel = name);

        plt.savefig(outputdir + '/' + name + '.png', dpi=300);
