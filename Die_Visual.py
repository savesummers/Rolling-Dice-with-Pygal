import pygal
from Rolling_Dice_with_Pygal import Die
Rolling_Dice_with_Pygal = Die()
results =[]
for roll_num in range(1000):
    result = Rolling_Dice_with_Pygal.roll()
    results.append(result)
print(results)

frequencies = [] 
for value in range(1, Rolling_Dice_with_Pygal.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)
print(frequencies)

hist = pygal.Bar()
hist.title='Bar Chart for Die Frequencies'
hist.x_labels= ['1','2','3','4','5','6']
hist.x_title = 'Values'
hist.y_title = 'Frequency'
hist.add('D6', frequencies)
hist.render_to_file('Die_Visual.svg')

    