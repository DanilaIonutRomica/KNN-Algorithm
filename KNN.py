import numpy as np
import matplotlib.pyplot as plt
import random 

def euclidian_distance(point_A,point_B):
    dimension = len(point_A)
    if dimension != len(point_B):
        return None
    sum=0
    for i in range(0,dimension):
        sum+= (point_A[i]-point_B[i]) **2
    return np.sqrt(sum)
    
def get_max_val_index_excluded(values):
    return values.index(max(values))

def vote(points,points_classes,point_to_clasify,k):
    distance_list=[]
    for point in points:
        distance_list.append(euclidian_distance(point,point_to_clasify))
    indexes=[]
    for i in range(0,k):
        index=get_max_val_index_excluded(distance_list)
        distance_list.remove(distance_list[index])
        indexes.append(index)
    count_Yes=0
    count_no=0
    for index in indexes:
        if points_classes[index] == "Yes":
            count_Yes+=1
        else:
            count_no+=1
    if count_Yes > count_no:
        return "Yes"
    else:
        return "No"

points=[]
red_class=[]
green_class=[]
classes=[]
for i in range(0,100):
    x=random.randint(1,1000)
    y=random.randint(1,1000)
    if x>500:
        classes.append("Yes")
        green_class.append([x,y])
    else:
        classes.append("No")
        red_class.append([x,y])
    points.append([x,y])


print(vote(points,classes,[720,100],50))
plt.plot(red_class,'o', color='red')
plt.plot(green_class,'o', color='green')
plt.plot([720,100],'o', color='blue')
plt.show()


        
        