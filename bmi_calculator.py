print("BMI CALCULATOR!")
weight=float(input("Enter your weight in kilograms:: "))
height=float(input("Enter your height in metre:: "))
try:
    if height <= 0 or weight <= 0:
        print("Error: Height and weight must be greater than zero.")
    else:
        bmi = weight / (height ** 2)
        print(f"BMI = {bmi}")
        
        if (bmi<18.5):
          print("Category= Underweight")

        elif (bmi>=18.5 and bmi<=24.9):
          print("Category= Normal Weight")

        elif (bmi>=25 and bmi<=29.9):
         print("Category= Overweight")
 
        elif (bmi>=30 and bmi<=34.9):
         print("Category= Obesity Class I (Mild)")

        elif (bmi>=35 and bmi<=39.9):
         print("Category= Obesity Class II (Severe)")
    
        else:
         print("Category= Obesity Class III (Very severe)")
    

except ValueError:
    print("Error: Please add correct values for height and weight ")
