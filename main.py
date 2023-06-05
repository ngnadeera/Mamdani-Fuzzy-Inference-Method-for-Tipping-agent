
from operator import xor

import numpy as np 
import skfuzzy as fuzz 
from skfuzzy import control as ctrl 
 
# Define the input variables 
food_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'food_quality') 
service_quality = ctrl.Antecedent(np.arange(0, 11, 1), 'service_quality') 
 
# Define the output variable 
tip = ctrl.Consequent(np.arange(0, 50, 1), 'tip') 
 
# Define the membership functions for the input variables 
food_quality['poor'] = fuzz.trimf(food_quality.universe, [0, 0, 5]) 
food_quality['average'] = fuzz.trimf(food_quality.universe, [0, 5, 10]) 
food_quality['excellent'] = fuzz.trimf(food_quality.universe, [5, 10, 10]) 
 
service_quality['poor'] = fuzz.trimf(service_quality.universe, [0, 0, 5]) 
service_quality['average'] = fuzz.trimf(service_quality.universe, [0, 5, 10]) 
service_quality['excellent'] = fuzz.trimf(service_quality.universe, [5, 10, 10]) 
 
# Define the membership functions for the output variable 
tip['low'] = fuzz.trimf(tip.universe, [0, 0, 25]) 
tip['medium'] = fuzz.trimf(tip.universe, [0, 25, 35]) 
tip['high'] = fuzz.trimf(tip.universe, [15, 35, 50]) /
 
# Define the rules 
rule1 = ctrl.Rule(food_quality['poor'] | service_quality['poor'], tip['low']) 
rule2 = ctrl.Rule(service_quality['average'], tip['medium']) 
rule3 = ctrl.Rule(food_quality['excellent'] | service_quality['excellent'], tip['high']) 
 
# Define the control system and add the rules 
tipping_ctrl = ctrl.ControlSystem([rule1, rule2, rule3]) 
 
# Create a simulation to test the system 
tipping = ctrl.ControlSystemSimulation(tipping_ctrl) 
x = 0
y = 0

x = int(input("Enter the Service Qulity (0-10)? :"))
y = x = int(input("Enter the Food Qulity? (0-10)? :"))

# Input some values 
tipping.input['food_quality'] = x
tipping.input['service_quality'] = y
 
# Crunch the numbers 
tipping.compute() 
 
# Output the result 
print("The recommended tip percentage is", tipping.output['tip'], "%")
