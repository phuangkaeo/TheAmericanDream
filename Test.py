# import Pandas as pd
import pandas as pd
# create a new data frame
s = pd.Series(["$46K-$87K (Glassdoor est.)", "$51K-$88K (Glassdoor est.)", "chameleon"])
print(s)

sl = s.str.slice(start=1, stop=3)
print(sl)

sl2 = s.str.slice(start=6, stop=8)
print(sl2)