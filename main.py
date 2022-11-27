import classes, requirements

myCompletedClasses = []

def main():
  print('--' * 20)
  print('Welcome to Finishing Computer Science B.S!')
  print('How can I help you?')
  print('--' * 20)

  while True:
    print("1. See available classes.\n2. See your remaining classes.\n\n(Enter any other value to exit.)")
    whatToDo = input("Enter: ")
    
    if whatToDo == "1":
      print('--' * 20)
      print('1. View University Core Requirements\n2. View Major Core Requirements')
      whichCoreRequirements = input("Enter: ")
      
      if whichCoreRequirements == "1":
        for myClass in classes.classList:
          if myClass["requirement"] == "University":
            print(myClass["course"], myClass["level"], "-", myClass["name"], "- Credit Hours:", myClass["creditHours"])
        print("-" * 20)
      elif whichCoreRequirements == "2":
        for myClass in classes.classList:
          if myClass["requirement"] == "Major":
            print(myClass["course"], myClass["level"], "-", myClass["name"], "- Credit Hours:", myClass["creditHours"])
        print("-" * 20)
      else:
        print("Error - Invalid option entered.")
    elif whatToDo == "2":
      print("--" * 20)
      print("Enter Classes Completed")
      
      while True:
        courseInput = input("Course (Ex. MATH): ")
        levelInput = input("Level (Ex. 2413): ")
        for myClass in classes.classList:
          if myClass["course"] == courseInput.strip().upper() and myClass["level"] == levelInput.strip() and myClass not in myCompletedClasses:
            myCompletedClasses.append(myClass)
            
        stop = input("Add more classes? (Y/N): ")
        print('--' * 20)
        
        if stop.strip().upper() != "Y":
          while True:
            viewInput = input("1. View your completed classes.\n2. View core complete status.\nEnter: ")
            if viewInput == "1":
              print("Your Completed Classes")
              print("--" * 20)
              for myClass in myCompletedClasses:
                print(myClass["course"], myClass["level"], "-", myClass["name"], "- Credit Hours:", myClass["creditHours"])
              print("--" * 20)
              break
            elif viewInput == "2":
              mathHours = 0
              commHours = 0
              lapsHours = 0
              lpacHours = 0
              artsHours = 0
              histHours = 0
              gposHours = 0
              sabsHours = 0
              comaHours = 0
              majorHours = 0
              
              for myClass in myCompletedClasses:
                if myClass["requirement"] == "University" and myClass["course"] == "MATH":
                  mathHours += myClass["creditHours"]
                elif myClass["requirement"] == "University" and myClass["course"] == "WRIT":
                  commHours += myClass["creditHours"]
                elif myClass["requirement"] == "University" and myClass["course"] == "PHYS":
                  lapsHours += myClass["creditHours"]
                elif myClass["requirement"] == "University" and myClass["course"] == ("ANTH" or "COMM" or "HUMN" or "LITR" or "PHIL" or "WGST"):
                  lpacHours += myClass["creditHours"]
                elif myClass["requirement"] == "University" and myClass["course"] == "ARTS":
                  artsHours += myClass["creditHours"]
                elif myClass["requirement"] == "University" and myClass["course"] == "HIST":
                  histHours += myClass["creditHours"]
                elif myClass["requirement"] == "University" and myClass["course"] == "POLS":
                  gposHours += myClass["creditHours"]
                elif myClass["requirement"] == "University" and myClass["course"] == ("CRIM" or "ECON" or "GEOG" or "PSYC" or "SOCI"):
                  sabsHours += myClass["creditHours"]
                elif myClass["requirement"] == "University" and (myClass["course"] == "COMM" and myClass["level"] == "1315") or (myClass["course"] == "PSYC" and myClass["level"] == "1100") or (myClass["course"] == "PHYS" and myClass["level"] == ("2125" or "2126")):
                  comaHours += myClass["creditHours"]
                elif myClass["requirement"] == "Major":
                  majorHours += myClass["creditHours"]
              
              print('--' * 20)
              if mathHours >= requirements.University["Mathematics"]:
                print("Mathematics: Complete")
              else:
                print("Mathematics: Incomplete")
                
              if commHours >= requirements.University["Communication"]:
                print("Communication: Complete")
              else:
                print("Communication: Incomplete")
              
              if lapsHours >= requirements.University["Life and Physical Sciences"]:
                print("Life and Physical Sciences: Complete")
              else:
                print("Life and Physical Sciences: Incomplete")
              
              if lpacHours >= requirements.University["Language, Philosophy and Culture"]:
                print("Language, Philosophy and Culture: Complete")
              else:
                print("Language, Philosophy and Culture: Incomplete")
              
              if artsHours >= requirements.University["Creative Arts"]:
                print("Creative Arts: Complete")
              else:
                print("Creative Arts: Incomplete")
              
              if histHours >= requirements.University["American History"]:
                print("American History: Complete")
              else:
                print("American History: Incomplete")
              
              if gposHours >= requirements.University["Government/Political Science"]:
                print("Government/Political Science: Complete")
              else:
                print("Government/Political Science: Incomplete")
              
              if sabsHours >= requirements.University["Social and Behavioral Sciences"]:
                print("Social and Behavioral Sciences: Complete")
              else:
                print("Social and Behavioral Sciences: Incomplete")
                
              if comaHours >= requirements.University["Component Area Option"]:
                print("Component Area Option: Complete")
              else:
                print("Component Area Option: Incomplete")
              
              if majorHours >= requirements.Major:
                print("Major Requirements: Complete")
              else:
                print("Major Requirements: Incomplete")
              print('--' * 20)
              
              break
            else:
              break
          break
    else:
      print("Thank you for using the class checker!")
      break
    
if __name__ == '__main__':
  main()