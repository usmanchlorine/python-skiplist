import random
import time
from wrapt_timeout_decorator import *

# roll Num 19B-072-CS , 19B-095-CS
# group 4

########## STACK ############ HELPING CLASS###
class Stack:

    def __init__(self,size):
        self.i = 0
        self.size=size
        self.data=[]
        for i in range(self.size):
            self.data.append(0)



    def IsEmpty(self):
        if self.i==0:
            return True
        return False

    def Push(self,item):
        if self.i!=self.size:
            self.data[self.i]=item
            # self.dic1={"(":")"}
            self.i=self.i+1
        else:
            if self.i == self.size:
                raise Exception(" stack is full")
    def IsFull(self):
        if self.i==self.size:
            return True
        return False
    def pop(self):
        if self.IsEmpty==True:
            raise Exception(" stack is undeflow")
        else:
            x=self.data[self.i-1]
            self.i=self.i-1
            return x
    def Peek(self):
        if self.IsEmpty() == True:
            return None

        else:
            x = self.data[self.i - 1]
            return x

    def Count(self):
        return self.i

    def Print(self):
        for numer in range(self.i):
            print(self.data[numer])



############ SKIPLIST ######### MAIN PROJECT #####



class Node :
    def __init__ ( self , value , height ) :
        self.height = height

        self.value = value
        self.next = None
        self.down = None


class Skiplist :
    def __init__ ( self , maxlevels ) :
        self.mexlevels = maxlevels           ## storing the max level
        value = float ( "-inf" )            ### initializing the value of negativeity
        sentinels = Node ( value , 0 )      ## creating the first node of sential
        self.head = sentinels               ### pointer self.head
        x = self.head                       ### creating the dummy point x  for self.head
        for i in range (1, maxlevels ) :
            value = float ( "-inf" )
            sentinels = Node ( value ,i )  ### make node  and put that node"s down point to x and over riding the previous sentinel
            sentinels.down = x
            x = sentinels                  ## update the x to node which we created back
        self.head = x                      ## update the self.head to most upward sentinel

    def Printsentinel ( self ) : ## this will prritn how many levels are created
        x = self.head
        while x!= None :
            print ( x.value , x.height )
            x = x.down

    def __pickheight ( self ) :
        list1 = ["head" , "tail"]
        k = 1
        while random.choice ( list1 ) == "head" :
            if k < self.mexlevels :  ## doing capping ( which means when k is above max level stop the height
                k += 1
        return k


    def Insert ( self , value ) :
        stack_list = Stack ( self.mexlevels )  ##  creating the stack  of max level
        k = self.__pickheight ( )    ### k is the height of particular node

        # print ( "kvalue", value , k )
        for i in range ( k) :  ## putting all node of (value) like if k =3  then 3 node of value "value" will be in stack
            newnode = Node ( value , i )
            stack_list.Push ( newnode )

        u = self.head ## y axis pointer
        x_axis = self.head  ## x axis pointer

        r = self.mexlevels-1

        while r >= 0 : ### itrate until the y pointer is on the level 0



            if r <=k-1 : ### if r <k-1 means you need to insert that node from stack to this level

                while (x_axis.next != None) and (x_axis.next.value <= value) : ### iterate horizontally  the reqiuired condition
                    x_axis = x_axis.next

                cur_node = stack_list.pop ( )

                old = x_axis.next
                x_axis.next = cur_node

                # print(cur_node.value)
                cur_node.next = old
                cur_node.down = stack_list.Peek ( ) ## linking down

            u = u.down ## changing y pointer
            x_axis = u ### changing x pointer to lvel-1
            r = r - 1

        return True

    def print_skiplist ( self ) :
        u = self.head ### y axis
        x_axis = self.head  ## x axis
        r = self.mexlevels-1  ### max level minus 1 because it will go NONE in last iteration  None do donot have next so it is pointing an error !!!!!
        while r >=0 :
            while x_axis != None :  ##  from every level -inf to None in x axis print the value of nodes
                print ( x_axis.value , end=" " )

                x_axis = x_axis.next

            u = u.down ## go down  level basically decreasing the levle height after every complete x axis traversal
            x_axis = u #### putting the x or updating the x axis to the down inf node for next x axis traversal
            print ( "\n" )
            r =r- 1 ### decreaseing the r increment if this not here the infinite loop will generate
#

    def __find_pred(self,value):
        try:
            u=self.head
            x_axis=self.head
            r=self.mexlevels-1
            while r>=0:

                while (x_axis.next!=None) and (x_axis.next.value<value):
                    x_axis=x_axis.next
                    u=x_axis


                r=r-1
                if u.down!=None: ### going down if.....
                    u=u.down
                if x_axis!=None:
                    x_axis=u
            return u
        except:
            return "something is Wrong"

    def find( self ,value):
        u=self.__find_pred(value)
        if u.next==None:
            return None
        if u.next.value==value:
            return u.next.value
        return None






    def Remove( self ,value):
        try:
            u = self.head  ## y axis pointer
            x_axis = self.head  ## x axis pointer

            r = self.mexlevels - 1

            while r >= 0 :  ### itrate until the y pointer is on the level 0



                while (x_axis.next != None) and (x_axis.next.value <= value) :

                    if x_axis.next.value==value:

                        x_axis.next = x_axis.next.next


                    else:
                        x_axis = x_axis.next
                        u=x_axis

                u = u.down  ## changing y pointer
                x_axis = u  ### changing x pointer to lvel-1
                r = r - 1
            return True
        except:
            return ("something is wrong try trying different value")



### TESTING FUNCTION ###


## printing sentinels along with their height checking if they are properly made

def test_1(total_height): # requires one argument!                              ## height checking of skip list
    test1= Skiplist ( total_height )
    test1.Printsentinel()


 ### checking the insertion function of skiplist  //// it will return  the skiplist of values you inserted in the skip list in Sorted Order
def test_2():
    h=int(input("enter the max of height of skiplist :"))
    test2=Skiplist(h)
    inserting_query=int(input("how many elements you want to insert? :"))
    for i in range(inserting_query):

        insert_value=int(input("enter the value you want to insert randomly ! : "))
        test2.Insert(insert_value)

    return test2.print_skiplist()

def test_3():
    test3=Skiplist(5)
    data = random.sample ( range ( 1 , 100 ) , 10 )
    for i in data:
        test3.Insert(i)

    test3.print_skiplist()
    removing_query=input(" do you want to remove an element y/n :")
    while removing_query=="y":
        removing_value=int(input("enter the value which you want to removed : "))
        test3.Remove(removing_value)
        removing_query = input ( " do you want to remove an element y/n :" )

    return test3.print_skiplist()


def test_4():
    test4=Skiplist(5)
    data = random.sample ( range ( 1 , 100 ) , 10 )
    for i in data:
        test4.Insert(i)

    test4.print_skiplist()
    removing_query=input(" do you want to find  an element y/n :")
    while removing_query=="y":
        finding_value=int(input("enter the value which you want to Find : "))
        print(test4.find(finding_value))
        removing_query = input ( " do you want to find an element y/n :" )






def test_timecomplexity():

    test4=Skiplist(7)
    data = random.sample ( range ( 1 , 8001 ) , 8000 )

    for i in data:
        test4.Insert(i)
    start = time.time ( )#starting time
    data2= random.sample ( range ( 1 , 8001 ) , 5 )
    for x in data2:
        test4.find ( x )
        test4.Remove(x)

    end = time.time ( ) ## ends with end time this technique is used by sir in class
    if abs(start-end)<=2:

        return True,abs(start-end)

    return False




# test_1(6)    ## checking the sentinel
#
# print(" ########## new test2 start########")
#
# test_2()     ## checking the insertion
#
# print(" ########## new test3 start########")
#
# test_3()      ## checkiing the removing
#
# print(" ########## new test4 start########")
#
# test_4()    ## checking the finding value
#
# print(" ########## new test_complexity start########")
#
#
# print(test_timecomplexity())   ## checking the complexity it will take some time
#






