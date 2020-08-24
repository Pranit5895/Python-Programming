print("The id() function in python");
print("");
print("In python, Rather than assigning different address for variables and let them act as containers for values as in cpp etc, Python uses pre-defined addresses for all values.");
print("In python, Variables are not a container and neither are they of any specific type so size of all variables in python is same");
print("It is because in python, variables are just simple pointers that point to pre-defined addressed values");

print(id("Pranit Gupta"));
var1 = "Pranit Gupta";
var2 = "Pranit Gupta";
var3 = "Pranit Gupta";
print(id(var1));
print(id(var2));
print(id(var3));
