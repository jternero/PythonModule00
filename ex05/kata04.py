kata = (0, 4, 132.42222, 10000, 12345.67)



module = "{:02d}".format(kata[0])
ex = "{:02d}".format(kata[1])
only_two_first = "{:.2f}".format(kata[2])
ten_elevated_four = "{:.2e}".format(kata[3])
num_x_ten_elevated_4 = "{:.2e}".format(kata[4])
print(f"module_{module}, ex_{ex} : {only_two_first}, {ten_elevated_four}, {num_x_ten_elevated_4}")
