num_list = [10,8,40, 10000, 16,25,23,30]
print (num_list[3:5])
i=0
gt_number=num_list[0]
for last_gt in num_list:
    print("looping inside" , last_gt)
    if last_gt > gt_number:
        gt_number = last_gt
    i=i+1

print(gt_number)