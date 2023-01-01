import os
import csv
from datetime import date
from dateutil import parser

inputdir = './data';
outpudir = './output';
for filename in os.listdir(inputdir):
    fp = os.path.join(inputdir, filename);
    if os.path.isfile(fp):
        with open(fp, newline='') as csvfile:
            reader = csv.DictReader(csvfile)

            fnameparts = filename.split('.');
            with open(outpudir + '/' + fnameparts[0] + '-processed' + '.' + fnameparts[1], 'w') as f:
                f.write('ADDRESS,URL,SOLD DATE,SOLD DATE MONTH,ZIP OR POSTAL CODE,YEAR BUILT,$/SQUARE FEET,$/SQUARE FEET Adjusted\n');

                for row in reader:
                    addr = row['ADDRESS'];
                    url = row['URL (SEE https://www.redfin.com/buy-a-home/comparative-market-analysis FOR INFO ON PRICING)']
                    sd = row['SOLD DATE'];
                    yb = row['YEAR BUILT'];
                    ps = row['$/SQUARE FEET'];

                    if not sd or not yb or not ps: continue; # skip no values
                    addr = addr.replace(',', '').replace('#', '');
                    sdparts = sd.split('-');
                    sm = '-'.join([sdparts[0], sdparts[2]]);

                    # update sold date format
                    sd = parser.parse(sd).strftime('%Y-%m-%d');

                    zip = row['ZIP OR POSTAL CODE'];
                    yb = int(float(yb));
                    pps = int(float(ps));

                    year = date.today().year
                    apps = pps + (year - yb);

                    f.write (','.join(map(str, [addr, url, sd, sm, zip, yb, pps, apps])) + '\n');
