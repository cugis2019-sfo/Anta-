#Day.4
import plotly
from plotly.offline import plot
import plotly.graph_objs as go


Studentlist = [["steve",32,"male"],["lia", 28,"female"],["vin",45,"male"],["katie",38,"female"]]
print(Studentlist)

studentlistdf = pandas.DataFrame(studentlist, columns = ["name","age","gender"], index = [1,2,3,4])
print(studentlistdf) 

import plotly
from plotly.offline import plot
import plotly.graph_objs as go

agename = go.Bar(x=studentlistdf["name"], y=studentlistdf["age"])

plot([agename])
























































