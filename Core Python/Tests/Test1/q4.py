#Calculate the cost of painting the following building's walls(both interior and exterior)
#You need to accept area(one wall) and cost of both interior and exterior wall
#note 1. below diagram is of two joint rooms
#2it is upper view of building

area=int(input('Enter Area of (one wall):'))
ec=int(input('Enter cost of exterior wall:'))
ic=int(input('Enter cost of interior wall:'))
ex_area=area*2
ic_area=area*2
ex_cost=ex_area*ec
ic_cost=ic_area*ic
print('Exterior cost=',ex_cost)
print('Interior cost=',ic_cost)
print('total=',ex_cost+ic_cost)
