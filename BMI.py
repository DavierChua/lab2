def calculate_bmi(height, weight):
 height1= height*height
 bmi= weight/height1
 return bmi
bmi0 = calculate_bmi(weight=57, height=1.73)
print("bmi=" + str(bmi0))
if bmi0<18.5 :
 print("Underweight")
elif 18.5<= bmi0 <= 25:
 print("acceptable") 
elif bmi0 > 25:
 print("Overweight")