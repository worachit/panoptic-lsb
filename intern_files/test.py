import matplotlib.pyplot as plt
plt.plot(
 [5, 4, 3], 
 [100, 200, 300] 
)
plt.title('Some Title')
plt.xlabel('Year')
plt.ylabel('Some measurements')
plt.savefig('my_plot.png')
plt.close()