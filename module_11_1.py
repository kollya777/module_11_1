import pandas as pd
import matplotlib.pyplot as plt

data = {
    'Продукт': ['Хлеб', 'Молоко', 'Колбаса', 'Сыр', 'Мясо'],
    'Продажи (шт.)': [10, 5, 15, 8, 20]
}
df = pd.DataFrame(data)

#Анализируем данные:
#Находим общий объём продаж:
total_sales = df['Продажи (шт.)'].sum()
print("Общий объём продаж:", total_sales)
#Вычисляем средний объём продаж по каждому продукту:
mean_sales = df['Продажи (шт.)'].mean()

#Строим график продаж по продуктам:
plt.bar(x=df['Продукт'], height=df['Продажи (шт.)'])
plt.title('Продажи по продуктам')
plt.xlabel('Продукт')
plt.ylabel('Продажи')
plt.show()