
#addition
def add(n1, n2) :
  return n1 + n2


#sub
def sub(n1, n2) :
  return n1 - n2


#divi
def divi(n1, n2) :
  return n1 / n2

#multi
def multi(n1, n2) :
  return n1 * n2


operations =  {
      "+" : add,
      "-" : sub,
      "*" : multi,
      "/" : divi,

}

num1 = int(input ( "What is the first number? : "))

num2 = int(input ( "What is the second  number? : "))

for symbol in operations : 
  print(symbol)

operation_symbol = input("pick an operation from the line above")

cal_fun =  operations [operation_symbol]
answer = cal_fun(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
