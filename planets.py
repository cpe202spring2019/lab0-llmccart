def weight_on_planets():
   weight = int(input('What do you weigh on earth?'))
   mars = weight*0.38
   jupiter = weight*2.34
   print('On Mars you would weigh %d pounds.' % mars)
   print('On Jupiter you would weigh %d pounds.' % jupiter)
   
   
if __name__ == '__main__':
   weight_on_planets()