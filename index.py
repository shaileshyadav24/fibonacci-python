def calculateFibonacci(numberTill):
    currentNumber = 1
    sum = 0
    previousNumber = 0
    while currentNumber < numberTill:
        sum = currentNumber + previousNumber
        print(currentNumber)
        previousNumber = currentNumber
        currentNumber = sum

t = input("Enter value till to display Fibonacci series: ") 
  
calculateFibonacci(int(t))