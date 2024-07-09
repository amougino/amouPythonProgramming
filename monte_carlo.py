import random
import matplotlib.pyplot as plt
import time

def average(numbers):
  if isinstance(numbers[0], list):
    average_list = []
    for row in numbers:
      a = 0
      for num in row:
        a += num
      average_list.append(a/len(row))
    return(average_list)
  else:
    a = 0
    for num in numbers:
      a += num
    return(a/len(numbers))

def median(numbers):
  if isinstance(numbers[0], list):
    median_list = []
    for row in numbers:
      median_list.append(row[int(len(row)/2)])
    return(median_list)
  else:
    return(numbers[int(len(numbers)/2)])

def monte_carlo(precision,ppl,start,iterations,modifiers):
  experiences = []
  startTime = time.time()
  for i in range(precision + 1):
    percent_bet = i/precision
    modifiers_it = (percent_bet * modifiers[0] + 1, percent_bet * modifiers[1] + 1)
    pop = [start for i in range(ppl)]
    for it in range(iterations):
      newPop = [pop[pers]*random.choice(modifiers_it) for pers in range(ppl)]
      pop = newPop.copy()
    time_since_start = time.time() - startTime
    print('remaining time :',((time_since_start/(i+1))*(precision - i))/60,'min',i)
    experiences.append(pop)
  average_experiences = average(experiences)
  median_experiences = median(experiences)

  plt.figure(1)
  plt.title('paradox average')
  plt.xlabel('Percent Bet')
  plt.ylabel('Average')
  x1 = [i/precision for i in range(precision + 1)]
  print(average_experiences)
  y1 = [(i/start)**(1/iterations+1) for i in average_experiences]
  plt.plot(x1, y1, color= 'aquamarine')

  plt.figure(2)
  plt.title('paradox median')
  plt.xlabel('Percent Bet')
  plt.ylabel('Median')
  x2 = [i/precision for i in range(precision + 1)]
  y2 = [(i/start)**(1/(iterations+1)) for i in median_experiences]
  #y2 = median_experiences
  print(y2)
  plt.plot(x2, y2, color= 'red')

  plt.show()

monte_carlo(500,10000,100,5000,(0.8,-0.5))