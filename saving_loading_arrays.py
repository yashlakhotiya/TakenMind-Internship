import numpy as np

# Saving single arrays

arr = np.arange(10)
print(arr)

#The RAM is limited. At a particular instant of time,we may not need full array in the main memory(RAM).
#So an alternative is to store thearray in the hard drive and retrieve it whenver required.
#And delete variable when we dont want it

np.save('saved_array',arr)
#New file is created - saved_array.npy in .npy format
#np.save take two arguments
#argument 1 is the name of .npy file
#argument 2 is the array which we want to store in the file

new_array = np.load('saved_array.npy')
#np.load will load the .npy file array which we created

print(new_array)

#Saving multiple arrays

#Multiple numpy arrays can be stored in a zip file

array_1 = np.arange(25)
array_2 = np.arange(30)

#np.savez('saved_archive.npz',array_1,array_2) This is wrong
np.savez('saved_archive.npz',x = array_1,y = array_2)
# np.savez is used to store multiple array
# npz is he file format which we use for savez function
load_archive = np.load('saved_archive.npz')
#load function is same for both single and multiple arrays
print("load_archive of x is")
print(load_archive['x'])

print("load_archive of y is")
print(load_archive['y'])

#We cannot see the .npy or .npz file in the system. And also, there is no text editor to read these files.
#For that, we have measure to convert them into text file

#Save to txtfile

np.savetxt('notepadfile.txt',array_1,delimiter=',')
#savetxt function takes three arguments
#arg1 is name of the file
#arg2 is the array which we want to store
#arg3 is the delimiter
#delimter is the character by which we want to separate the array in txt file


# loading of txt files

load_txt_file = np.loadtxt('notepadfile.txt',delimiter=',')
#loadtxt function has two argumnts
#arg1 is name of file
#arg2 is delimiter which computer should know so that it will decode the array

print("load_txt_file is")
print(load_txt_file)

# After printing the array using loadtxt function, its is howing float values instead of integer values because
# when we use loadtxt function, it cob=nverts integer to float datatype

