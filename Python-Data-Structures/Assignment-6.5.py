# Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. Convert the extracted value to a floating poinit number and print it out.





# code 
text = "X-DSPAM-Confidence:    0.8475";
aa = text.find ('0')
bb = text.find ('', aa)
number = text [aa:]
n = float(number)
print (n)
