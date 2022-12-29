
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

num1 = int(input ( "What is the first number? :\n "))

num2 = int(input ( "What is the second  number? :\n "))

for symbol in operations : 
  print(symbol)

operation_symbol = input("pick an operation from the line above : \n")

cal_fun =  operations [operation_symbol]
answer = cal_fun(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")

 
operation_symbol = input("pick another operation")

num3 = int(input ( "Another number? :\n "))

cal_fun =  operations [operation_symbol]

second_answer = cal_fun(answer, num3)

print(f"{answer} {operation_symbol} {num3} = {second_answer}")




