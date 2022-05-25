import os
class water:
    #init function
    def __init__(self):
        self.guest=0
        self.total_water_2=900
        self.total_water_3=1500
        self.total_guest=0
        self.corporation_amount_2=0
        self.borewell_amount_2=0
        self.corporation_amount_3=0
        self.borewell_amount_3=0


    #this function will allot the water to apartement and distribute according to ratio passed    
    def allotwater(self,apartment_type,ratio):
        ratio=ratio.split(":")
        ratio=[int(i) for i in ratio]
        if apartment_type==2:
            self.corporation_amount_2=(self.total_water_2*ratio[0])//sum(ratio)
            self.borewell_amount_2=(self.total_water_2*ratio[1])//sum(ratio)
            
        else:
            self.corporation_amount_3=(self.total_water_3*ratio[0])//sum(ratio)
            self.borewell_amount_3=(self.total_water_3*ratio[1])//sum(ratio)
            

    #this function will add_guest as mentioned in the requirement
    def add_guest(self,guest_number):
        self.total_guest+=guest_number

    #this function will generate the bill for total water used
    def bill(self):
        guest_total_cost=0
        guest_total_water=self.total_guest*30*10
        #while guest_total_water>0:

        if(guest_total_water>=0 and guest_total_water<=500):
            guest_total_cost+=guest_total_water*2

        elif(guest_total_water>=501 and guest_total_water<=1500):
            guest_total_cost+=(500*2)+(guest_total_water-500)*3
      
        elif(guest_total_water>=1501 and guest_total_water<=3000):
            guest_total_cost+=(500*2)+(guest_total_water-500)*3+(guest_total_water-1500)*5
        else:
            guest_total_cost+=(500*2)+(guest_total_water-500)*3+(guest_total_water-1500)*5+(guest_total_water-3000)*8
    

        apartment_2=(self.corporation_amount_2+self.corporation_amount_3)*1
        apartment_3=(self.borewell_amount_2 + self.borewell_amount_3)*1.5
    

        apartment_total_water=self.corporation_amount_2+self.corporation_amount_3+self.borewell_amount_2+self.borewell_amount_3
        total_water_used=apartment_total_water+guest_total_water
        total_cost=guest_total_cost+apartment_2+apartment_3
        return [total_water_used,int(total_cost)]

if __name__ =='__main__':
    water=water()
    path=input("Enter the test file Path")
    os.chdir(path)
    if os.path.exists(path):

        f=open(path)
        c=f.read()
        c=c.split()
        for i in range(len(c)):
            if c[i]=="Allotwater":
                apartment_type=int(c[i+1])
                ratio=c[i+2]
                water.allotwater(apartment_type,ratio)
            if c[i]=="add_guest":
                guest_number=int(c[i+1])
                water.add_guest(guest_number)
            if c[i]=="bill":
                a=water.bill()
        print(a)
        f.close()
        #this function can be used when you want to save the output to the particular file
        # output=open("D:/DSA/Array/final_output.txt","w")
        # for i in a:
        #     output.write(str(i))
        #     output.write(" ")
        # output.close()
    else:
        print("This test file path does not exist")




            

