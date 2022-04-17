def errorCheck(firstValue,operator,secondValue):
  maxDigits = 4
  try:
    int(firstValue)
  except:
    return("Error: Numbers must only contain digits.")
  try:
    int(secondValue)
  except:
    return("Error: Numbers must only contain digits.")
  try:
    if len(firstValue) > maxDigits or len(secondValue) > maxDigits:
      raise BaseException
  except:    
    return("Error: Numbers cannot be more than four digits.")
  try:
    if operator not in "-+":
      raise BaseException
  except:
    return("Error: Operator must be '+' or '-'.")
  return("")

def arithmetic_arranger(problems, displayData = False):

  #defining objects to build the funtion
  lengthOfProblems = 5
  line1 = ""
  line2 = ""
  line3 = ""
  line4 = ""
  sideSpace = "    "
  space = ""
  start = True
  
#Error Checks Start 
  try:
    if len(problems) > lengthOfProblems:
      raise BaseException
  except:
    return "Error: Too many problems."
  #Looping through to grab all the information. Dont forget to indent correctly.  
  for problem in problems:
    #("32","+","698")
    splitString = problem.split()
    firstValue = splitString[0]
    operator = splitString[1]
    secondValue = splitString[2]
    
    #Grabs the error list from the def above
    errorDef = errorCheck(firstValue,operator,secondValue)
    if errorDef != (""):
      return errorDef
#Error Check Ends
      
  #giving values to the objects in problems
    firstValueInt  = int(firstValue)
    secondValueInt = int(secondValue)
    space = max(len(firstValue), len(secondValue))
  
  #First line is different for how the information is shown than the rest
    if start == True:
      line1 =  firstValue.rjust(space + 2)
      line2 = operator + " " + secondValue.rjust(space)
      line3 = "-" * (space + 2)
      if displayData == True :
        if operator == "+" :
          line4 = str(firstValueInt + secondValueInt).rjust(space + 2)
        elif operator == "-":
          line4 = str(firstValueInt - secondValueInt).rjust(space + 2)
      start = False
    
  #provides the rest of the information
    else:
      line1 = line1 + firstValue.rjust(space + 6)
      line2 = line2 + operator.rjust(5) + ' ' + secondValue.rjust(space)
      line3 = line3 + sideSpace + '-' * (space + 2)
      if displayData == True:
        if operator == '+':
          line4 = line4 + sideSpace + str(firstValueInt + secondValueInt).rjust(space + 2)
        else:
          line4 = line4 + sideSpace + str(firstValueInt - secondValueInt).rjust(space + 2)

  if displayData == True:
    return line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
  return line1 + "\n" + line2 + "\n" + line3
  
  #Start of the arithmetic_arranger
  #Calculate the lenth of each line
  #Add spaces to each line
  #generate the correct number of dashes below the problems statement
  #Append the answer if needed
