import csv
import pandas as pd
import plotly.figure_factory as ff
import statistics

cd = pd.read_csv("height-weight.csv")

height_list = cd["Height(Inches)"].tolist()
weight_list = cd["Weight(Pounds)"].tolist()

h_mean = statistics.mean(height_list)
w_mean = statistics.mean(weight_list)

h_median = statistics.median(height_list)
w_median = statistics.median(weight_list)

h_mode = statistics.mode(height_list)
w_mode = statistics.mode(weight_list)

h_std_dev = statistics.stdev(height_list)
w_std_dev = statistics.stdev(weight_list)

print("Mean,mode,median and standard devoiation of height is {} , {} , {} and {}".format(h_mean,h_median,h_mode,h_std_dev))
print("Mean,mode,median and standard devoiation of Weight is {} , {} , {} and {}".format(w_mean,w_median,w_mode,w_std_dev))

#fig = ff.create_distplot([cd["Avg Rating"].tolist()],["Brand"])

#fig.show()

f_h_stdev_start,f_h_stdev_end = h_mean - h_std_dev,h_mean + h_std_dev
s_h_stdev_start,s_h_stdev_end = h_mean - (2*h_std_dev),h_mean + (2*h_std_dev)
t_h_stdev_start,t_h_stdev_end = h_mean - (3*h_std_dev),h_mean + (3*h_std_dev)

f_w_stdev_start,f_w_stdev_end = w_mean - w_std_dev,w_mean + w_std_dev
s_w_stdev_start,s_w_stdev_end = w_mean - (2*w_std_dev),w_mean + (2*w_std_dev)
t_w_stdev_start,t_w_stdev_end = w_mean - (3*w_std_dev),w_mean + (3*w_std_dev)

h_1_std_dev = [result for result in height_list if result>f_h_stdev_start and result<f_h_stdev_end]
h_2_std_dev = [result for result in height_list if result>s_h_stdev_start and result<s_h_stdev_end]
h_3_std_dev = [result for result in height_list if result>t_h_stdev_start and result<t_h_stdev_end]

w_1_std_dev = [result for result in weight_list if result>f_w_stdev_start and result<f_w_stdev_end]
w_2_std_dev = [result for result in weight_list if result>s_w_stdev_start and result<s_w_stdev_end]
w_3_std_dev = [result for result in weight_list if result>t_w_stdev_start and result<t_w_stdev_end]

print("{}% of data for height lies within 1 standard deviation".format(len(h_1_std_dev)*100.0/len(height_list)))
print("{}% of data for height lies within 2 standard deviation".format(len(h_2_std_dev)*100.0/len(height_list)))
print("{}% of data for height lies within 3 standard deviation".format(len(h_3_std_dev)*100.0/len(height_list)))

print("{}% of data for weight lies within 1 standard deviation".format(len(w_1_std_dev)*100.0/len(weight_list)))
print("{}% of data for weight lies within 2 standard deviation".format(len(w_2_std_dev)*100.0/len(weight_list)))
print("{}% of data for weight lies within 3 standard deviation".format(len(w_3_std_dev)*100.0/len(weight_list)))














