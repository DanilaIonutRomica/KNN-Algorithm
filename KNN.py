import numpy as np
import matplotlib.pyplot as plt
import random 
import math

class KNN:
    def __init__(self,K,list_of_points,points_classes,classes_names,point_to_clasifiy,distance="euclidian",classes_color=None):
        self.k=K
        self.points=list_of_points
        self.distance=distance
        self.point_to_clasifiy=point_to_clasifiy
        self.points_classes=points_classes
        self.classes_names=classes_names
        self.close_points=[]
        self.classes_color=classes_color
    def calculate_distance(self,point_A,point_B,distance="euclidian"):
        dimension = len(point_A)
        if dimension != len(point_B):
            return None
        if distance == "euclidian":
            sum=0
            for i in range(0,dimension):
                sum+= (point_A[i]-point_B[i])**2
            return np.sqrt(sum)
        if distance.startswith("L"):
            distance=distance.replace("L","")
            pr=float(distance)
            sum=0
            for i in range(0,dimension):
                sum+=math.pow( np.abs(point_A[i] - point_B[i]),pr)
            return sum
    def get_max_val_index_excluded(self,values,excluded):
        if excluded == []: 
            return values.index(min(values))
        else:
            index_min=0
            minm=values[0]
            for i in range(0,len(values)):
                if values[i]<minm and i not in excluded:
                    minm=values[i]
                    index_min=i
            return index_min
    def vote(self):
        distance_list=[]
        for point in self.points:
            distance_list.append(self.calculate_distance(point,self.point_to_clasifiy,self.distance))
        indexes=[]
        excluded_indexs=[]
        for i in range(0,self.k):
            index=self.get_max_val_index_excluded(distance_list,excluded_indexs)
            self.close_points.append(points[index])
            excluded_indexs.append(index)
            indexes.append(index)
        my_classes_counts={}
        for elem in self.classes_names:
            my_classes_counts[elem]= 0
        for index in indexes:
            for elem in my_classes_counts:
                if self.points_classes[index] == elem:
                    my_classes_counts[elem]+=1
        return max(my_classes_counts, key=my_classes_counts.get)

    def show_plt(self):
        dimension=len(self.point_to_clasifiy)
        for i in range(0,len(self.points)):
            plt.plot(self.points[i][0],self.points[i][1],'o',color=self.classes_color[self.points_classes[i]])
        for i in range(0,len(self.close_points)):
            plt.plot(self.close_points[i][0],self.close_points[i][1],'o',color="black")
        plt.plot(self.point_to_clasifiy[0],self.point_to_clasifiy[1],'o',color="blue")
        plt.show()
                    
            
points=[]
classes=[]

for i in range(0,5000):
    x=random.randint(0,100)
    y=random.randint(0,100)
    if x>50:
        classes.append("Yes")
    else:
        classes.append("No")
    points.append([x,y])

knn=KNN(500,points,classes,["Yes","No"],[50,50],classes_color={"Yes" : "green" ,"No" : "red"})
print(knn.vote())
knn.show_plt()

        
        