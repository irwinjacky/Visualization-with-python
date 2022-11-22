# %%
print('Visualization with python')
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
#importing data
data = pd.read_csv('breast-cancer.data')
data.columns = ['class', 'age', 'menopause', 'tumor_size', 'inv_nodes', 'node_caps', 'deg_malig', 'breast', 'breast_quad', 'irradiat']

print(data.columns)


# %%
#group data want to show in pie chart
pi_data = data.groupby('class').sum()
y_one = pi_data.values.flatten()
#find the labels
labels_one = pi_data.index

#plot the pie chart
plt.pie(y_one, labels = labels_one)
plt.title('recurrence to degree of malignant')
plt.legend(title = 'Class')
plt.show()

# %%
#find group data for bar chart
bar_data = data.groupby('age').count()
age_bar_dat = bar_data['class']

#break data into peices
age_one = age_bar_dat.values
age_b = age_bar_dat.index

#create font
font1 = {'family' : 'serif', 'color' : 'red', 'size' : 20}
font2 = {'family' : 'serif', 'color': 'green', 'size' : 10}

#plot the bar graph
plt.bar(age_b, age_one)
#title the graph
plt.title('Age of Participants', fontdict = font1)
#label the axis
plt.xlabel('Age range', fontdict = font2)
plt.ylabel('Number of Participants', fontdict = font2)
plt.show()

# %%

line_data = data.groupby(['menopause','age']).sum()
line_y = line_data.values.flatten()

line_ya = line_y[:4]
line_yb = line_y[4:7]
line_yc = line_y[7:]
#line_x = list(line_data.index)
#line_xa = line_x[:4]
#line_xb = line_x[4:7]
#line_xc = line_x[7:]

x_alist = ['40-49', '50-59', '60-69', '70-79']
x_blist = ['30-39', '50-59', '60-69']
x_clist = ['20-29', '30-39', '40-49', '50-59']

plt.scatter(x_alist, line_ya, color = 'red')
plt.scatter(x_blist, line_yb, color = 'cyan')
plt.scatter(x_clist, line_yc, color = 'green')
plt.title('menopause vs age vs degree of malignancy', fontdict = font1)
plt.legend(title ='menopause')
plt.xlabel('Age')
plt.ylabel('degree of malignant')
plt.show()

# %%
linea_one = data.groupby('inv_nodes').count()
line_one = linea_one['class']
line_data = line_one.index
line_bdata = line_one.values

plt.plot(line_data, line_bdata)
plt.grid()
plt.title('apperance of different amount of nodes', fontdict = font1)
plt.xlabel('amount of invidule nodes', color = 'purple')
plt.ylabel('cases of nodes apperence in study')
plt.show()

# %%



