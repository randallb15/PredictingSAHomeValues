import glob
import pandas as pd

path =r'/Users/randallbloomquist/Desktop/Desktop/Galvanize/CAPSTONES/Sell Your Home in 30 days/data'
all_files = glob.glob(path + "/*.csv")
df = pd.DataFrame()
df = df.iloc[0:0]
for file_ in all_files:
    print(file_)
    df.drop(df.index, inplace=True)
    df = pd.concat((pd.read_csv(f) for f in all_files))
    
df.drop(['NEXT OPEN HOUSE START TIME','NEXT OPEN HOUSE END TIME','URL (SEE http://www.redfin.com/buy-a-home/comparative-market-analysis FOR INFO ON PRICING)','SOURCE','FAVORITE','INTERESTED'], axis=1,inplace=True)
df.drop_duplicates(inplace=True)
df.to_pickle('data/full.pkl')