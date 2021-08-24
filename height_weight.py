# normal distribution is something that helps us extracting the pattern in the dataset
# normal distribution can be seen as a probability distribution where mean=median=mode in a normal distribution and corresponds to the peak value written
# normal distribution is symmetric around the peak value. 68% of all data lies within 1 standrd deviation of the mean
# 95% of the data lies within 2 standard deviation of the mean
# 99% of the data lies within 3 standard deviation of the mean

  
import pandas as pd
import statistics
import csv

df = pd.read_csv("data.csv")

height_list = df["Height(Inches)"].to_list()
weight_list = df["Weight(Pounds)"].to_list()

# mean for height and weight
height_mean = statistics.mean(height_list)
weight_mean = statistics.mean(weight_list)

# median for height and weight
height_median = statistics.median(height_list)
weight_median = statistics.median(weight_list)

# mode for height and weight
height_mode = statistics.mode(height_list)
weight_mode = statistics.mode(weight_list)

#printing mean,median,mode for height to validate 
print("Mean, median, mode of height is: {}, {}, {} respectively".format(height_mean, height_median, height_mode))

#printing mean,median mode for weight to validate
print("Mean, median, mode of weight is: {}, {}, {} respectively".format(weight_mean, weight_median, weight_mode))

# standard deviation for height and weight
height_std_deviation = statistics.stdev(height_list)
weight_std_deviation = statistics.stdev(weight_list)

# 1 standard deviations for height and weight
height_first_std_deviation_start, height_first_std_deviation_end = height_mean - height_std_deviation, height_mean + height_std_deviation
weight_first_std_deviation_start, weight_first_std_deviation_end = weight_mean - weight_std_deviation, weight_mean + weight_std_deviation

# 2 standard deviations for height and weight
height_second_std_deviation_start, height_second_std_deviation_end = height_mean - (2* height_std_deviation), height_mean + (2* height_std_deviation)
weight_second_std_deviation_start, weight_second_std_deviation_end = weight_mean - (2* weight_std_deviation), weight_mean + (2* weight_std_deviation)

# 3 standard deviations for height and weight
height_third_std_deviation_start, height_third_std_deviation_end = height_mean - (3* height_std_deviation), height_mean + (3* height_std_deviation)
weight_third_std_deviation_start, weight_third_std_deviation_end = weight_mean - (3* weight_std_deviation), weight_mean + (3* weight_std_deviation)

# percentage of data within 1,2,3 standard deviations for height 
height_list_of_data_within_1_std_deviation = [result for result in height_list if result > height_first_std_deviation_start and result < height_first_std_deviation_end]
height_list_of_data_within_2_std_deviation = [result for result in height_list if result > height_second_std_deviation_start and result < height_second_std_deviation_end]
height_list_of_data_within_3_std_deviation = [result for result in height_list if result > height_third_std_deviation_start and result < height_third_std_deviation_end]

# percentage of data within 1,2,3 standard deviations for weight
weight_list_of_data_within_1_std_deviation = [result for result in weight_list if result > weight_first_std_deviation_start and result < weight_first_std_deviation_end]
weight_list_of_data_within_2_std_deviation = [result for result in weight_list if result > weight_second_std_deviation_start and result < weight_second_std_deviation_end]
weight_list_of_data_within_3_std_deviation = [result for result in weight_list if result > weight_third_std_deviation_start and result < weight_third_std_deviation_end]

# printing the data for height % within 1,2,3 standard deviations
print("{}% of data for height lies within 1 standard deviation ".format(len(height_list_of_data_within_1_std_deviation) * 100.0 / len(height_list)))
print("{}% of data for height lies within 2 standard deviations ".format(len(height_list_of_data_within_2_std_deviation) * 100.0 / len(height_list)))
print("{}% of data for height lies within 3 standard deviations ".format(len(height_list_of_data_within_3_std_deviation) * 100.0 / len(height_list)))

# printing the data for weight % withing 1,2,3 standard deviations
print("{}% of data for weight lies within 1 standard deviation ".format(len(weight_list_of_data_within_1_std_deviation) * 100.0 / len(weight_list)))
print("{}% of data for weight lies within 2 standard deviations ".format(len(weight_list_of_data_within_2_std_deviation) * 100.0 / len(weight_list)))
print("{}% of data for weight lies within 3 standard deviations ".format(len(weight_list_of_data_within_3_std_deviation) * 100.0 / len(weight_list)))
