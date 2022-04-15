#mean calculator for "4" number

mean1 = input("Enter the first number you would like to find the average for: ")

mean2 = input("Enter the second number you would like to find the average for: ")

mean3 = input("Enter the third number you would like to find the average for: ")

mean4 = input("Enter the fourth number you would like to find the average for: ")

mean1 = int(mean1)
mean2 = int(mean2)
mean3 = int(mean3)
mean4 = int(mean4)


pre_mean = mean1 + mean2 + mean3 + mean4
mean = pre_mean / 4

print(f"The mean of your input is {mean}")
