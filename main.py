# ======================================================================
# ПРАКТИЧНА РОБОТА № 9-10
# Тема: Візуалізація даних у Python
#
# Виконано за допомогою:
# - Matplotlib
# - Seaborn
# - Plotly
#
# Для запуску:
# pip install matplotlib seaborn plotly pandas numpy
# ======================================================================

# ======================================================================
# ІМПОРТ БІБЛІОТЕК
# ======================================================================

import matplotlib
matplotlib.use('TkAgg')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# ======================================================================
# НАЛАШТУВАННЯ СТИЛЮ
# ======================================================================

plt.style.use('ggplot')

# ======================================================================
# ЗАВДАННЯ 1
# Побудувати в одній системі координат лінійні графіки функцій:
# y1 = sin(x)
# y2 = sin(2x + π/4)
# y3 = cos(3x - π/3)
#
# На інтервалі:
# x ∈ [-2π ; 2π]
# з кроком 0.5
# ======================================================================

print("=" * 80)
print("ЗАВДАННЯ 1")
print("Побудова лінійних графіків функцій")

x = np.arange(-2 * np.pi, 2 * np.pi + 0.5, 0.5)

y1 = np.sin(x)
y2 = np.sin(2 * x + np.pi / 4)
y3 = np.cos(3 * x - np.pi / 3)

plt.figure(figsize=(14, 7))

plt.plot(
    x,
    y1,
    color='blue',
    linestyle='-',
    linewidth=2,
    marker='o',
    markersize=6,
    label='y = sin(x)'
)

plt.plot(
    x,
    y2,
    color='red',
    linestyle='--',
    linewidth=2,
    marker='s',
    markersize=6,
    label='y = sin(2x + π/4)'
)

plt.plot(
    x,
    y3,
    color='green',
    linestyle=':',
    linewidth=2,
    marker='^',
    markersize=6,
    label='y = cos(3x - π/3)'
)

plt.title("Лінійні графіки функцій", fontsize=18)
plt.xlabel("x", fontsize=14)
plt.ylabel("y", fontsize=14)

plt.grid(True)
plt.legend(fontsize=12)

plt.annotate(
    'Максимум sin(x)',
    xy=(1.5, 1),
    xytext=(3, 1.2),
    arrowprops=dict(facecolor='black', shrink=0.05),
    fontsize=12
)

plt.show()

print("Завдання 1 виконано успішно")

# ======================================================================
# ЗАВДАННЯ 2
# Побудувати діаграми розсіювання
# ======================================================================

print("=" * 80)
print("ЗАВДАННЯ 2")
print("Побудова діаграм розсіювання")

data = {
    'Country': [
        'Germany',
        'France',
        'Italy',
        'Spain',
        'Poland',
        'Romania',
        'Czechia',
        'Sweden',
        'Belgium',
        'Netherlands'
    ],

    'GDP': [
        3800,
        2600,
        1900,
        1300,
        600,
        250,
        245,
        530,
        520,
        910
    ],

    'Population': [
        83,
        67,
        60,
        47,
        38,
        19,
        10,
        10,
        11,
        17
    ],

    'GDP_per_capita': [
        46000,
        39000,
        32000,
        28000,
        16000,
        13000,
        23000,
        52000,
        47000,
        53000
    ],

    'Life_expectancy': [
        81,
        82,
        83,
        83,
        78,
        76,
        79,
        82,
        81,
        82
    ],

    'Health_spending': [
        5700,
        5000,
        3400,
        3000,
        2200,
        1700,
        2500,
        6000,
        5400,
        6100
    ],

    'Category': [
        1,
        1,
        1,
        2,
        3,
        3,
        3,
        2,
        1,
        1
    ]
}

df = pd.DataFrame(data)

# ----------------------------------------------------------------------
# ДІАГРАМА 1
# ВВП та кількість населення
# ----------------------------------------------------------------------

plt.figure(figsize=(12, 7))

plt.scatter(
    df['Population'],
    df['GDP'],
    color='blue',
    s=150,
    edgecolors='black'
)

for i in range(len(df)):
    plt.text(
        df['Population'][i],
        df['GDP'][i],
        df['Country'][i],
        fontsize=9
    )

plt.title("ВВП та населення країн ЄС", fontsize=18)
plt.xlabel("Населення, млн", fontsize=14)
plt.ylabel("ВВП, млрд доларів", fontsize=14)

plt.grid(True)

plt.show()

# ----------------------------------------------------------------------
# ДІАГРАМА 2
# ВВП на душу населення та середня тривалість життя
# ----------------------------------------------------------------------

colors = {
    1: 'red',
    2: 'green',
    3: 'blue'
}

plt.figure(figsize=(12, 7))

for category in df['Category'].unique():

    subset = df[df['Category'] == category]

    plt.scatter(
        subset['GDP_per_capita'],
        subset['Life_expectancy'],
        s=subset['Health_spending'] / 10,
        c=colors[category],
        alpha=0.7,
        edgecolors='black',
        label=f'Категорія {category}'
    )

for i in range(len(df)):
    plt.text(
        df['GDP_per_capita'][i],
        df['Life_expectancy'][i],
        df['Country'][i],
        fontsize=9
    )

plt.title(
    "ВВП на душу населення та тривалість життя",
    fontsize=18
)

plt.xlabel("ВВП на душу населення", fontsize=14)
plt.ylabel("Середня тривалість життя", fontsize=14)

plt.legend(fontsize=11)
plt.grid(True)

plt.show()

print("Завдання 2 виконано успішно")

# ======================================================================
# ЗАВДАННЯ 3
# Побудувати горизонтальну стовпчикову діаграму
# ======================================================================

print("=" * 80)
print("ЗАВДАННЯ 3")
print("Побудова горизонтальної стовпчикової діаграми")

countries = ['Poland', 'Romania', 'Czechia']
gdp_values = [16000, 13000, 23000]

plt.figure(figsize=(10, 6))

bars = plt.barh(
    countries,
    gdp_values,
    color=['blue', 'green', 'red'],
    edgecolor='black',
    label='GDP per capita'
)

plt.title(
    "ВВП на душу населення за 2020 рік",
    fontsize=18
)

plt.xlabel("ВВП на душу населення", fontsize=14)
plt.ylabel("Країни", fontsize=14)

plt.legend()
plt.grid(True)

plt.show()

print("Завдання 3 виконано успішно")

# ======================================================================
# ЗАВДАННЯ 4
# Групова стовпчикова діаграма
# ======================================================================

print("=" * 80)
print("ЗАВДАННЯ 4")
print("Групова стовпчикова діаграма")

countries = [
    'Germany',
    'France',
    'Czechia',
    'Poland',
    'Romania'
]

gdp_2010 = [42000, 41000, 18000, 12000, 9000]
gdp_2015 = [45000, 43000, 20000, 14000, 10000]
gdp_2020 = [46000, 39000, 23000, 16000, 13000]

x = np.arange(len(countries))

width = 0.22

plt.figure(figsize=(14, 7))

plt.bar(
    x - width,
    gdp_2010,
    width,
    color='blue',
    label='2010'
)

plt.bar(
    x,
    gdp_2015,
    width,
    color='green',
    label='2015'
)

plt.bar(
    x + width,
    gdp_2020,
    width,
    color='red',
    label='2020'
)

plt.xticks(x, countries)

plt.title(
    "ВВП на душу населення",
    fontsize=18
)

plt.xlabel("Країни", fontsize=14)
plt.ylabel("ВВП", fontsize=14)

plt.legend(fontsize=12)
plt.grid(True)

plt.show()

print("Завдання 4 виконано успішно")

# ======================================================================
# ЗАВДАННЯ 5
# Кругові діаграми структури ВВП
# ======================================================================

print("=" * 80)
print("ЗАВДАННЯ 5")
print("Кругові діаграми структури ВВП")

labels = [
    'Промисловість',
    'Сільське господарство',
    'Послуги'
]

world = [28, 4, 68]
europe = [25, 2, 73]
ukraine = [20, 10, 70]

fig, axs = plt.subplots(1, 3, figsize=(18, 7))

# ----------------------------------------------------------------------
# Світ
# ----------------------------------------------------------------------

axs[0].pie(
    world,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90
)

axs[0].set_title("Світ")

# ----------------------------------------------------------------------
# Європа
# ----------------------------------------------------------------------

axs[1].pie(
    europe,
    labels=labels,
    shadow=True,
    startangle=90
)

axs[1].set_title("Європа")

# ----------------------------------------------------------------------
# Україна
# ----------------------------------------------------------------------

explode = (0.1, 0, 0)

axs[2].pie(
    ukraine,
    labels=labels,
    explode=explode,
    startangle=90
)

axs[2].set_title("Україна")

plt.show()

print("Завдання 5 виконано успішно")

# ======================================================================
# ЗАВДАННЯ 6
# Групова стовпчикова діаграма з накопиченням
# ======================================================================

print("=" * 80)
print("ЗАВДАННЯ 6")
print("Стовпчикова діаграма з накопиченням")

countries = [
    'USA',
    'Germany',
    'Turkey',
    'Poland',
    'Ukraine'
]

industry_2010 = [20, 31, 30, 29, 26]
agriculture_2010 = [1, 1, 8, 4, 12]
services_2010 = [79, 68, 62, 67, 62]

industry_2020 = [19, 30, 32, 28, 25]
agriculture_2020 = [1, 1, 6, 3, 10]
services_2020 = [80, 69, 62, 69, 65]

x = np.arange(len(countries))

width = 0.35

fig, ax = plt.subplots(figsize=(14, 8))

# ----------------------------------------------------------------------
# 2010
# ----------------------------------------------------------------------

ax.bar(
    x - width / 2,
    industry_2010,
    width,
    label='Промисловість 2010',
    color='blue'
)

ax.bar(
    x - width / 2,
    agriculture_2010,
    width,
    bottom=industry_2010,
    label='С/Г 2010',
    color='green'
)

bottom_2010 = np.array(industry_2010) + np.array(agriculture_2010)

ax.bar(
    x - width / 2,
    services_2010,
    width,
    bottom=bottom_2010,
    label='Послуги 2010',
    color='cyan'
)

# ----------------------------------------------------------------------
# 2020
# ----------------------------------------------------------------------

ax.bar(
    x + width / 2,
    industry_2020,
    width,
    label='Промисловість 2020',
    color='red'
)

ax.bar(
    x + width / 2,
    agriculture_2020,
    width,
    bottom=industry_2020,
    label='С/Г 2020',
    color='orange'
)

bottom_2020 = np.array(industry_2020) + np.array(agriculture_2020)

ax.bar(
    x + width / 2,
    services_2020,
    width,
    bottom=bottom_2020,
    label='Послуги 2020',
    color='pink'
)

ax.set_xticks(x)
ax.set_xticklabels(countries)

ax.set_title(
    "Структура ВВП у 2010 та 2020 роках",
    fontsize=18
)

ax.set_xlabel("Країни", fontsize=14)
ax.set_ylabel("Частка у ВВП (%)", fontsize=14)

ax.legend(fontsize=10)

plt.show()

print("Завдання 6 виконано успішно")

# ======================================================================
# ЗАВДАННЯ 7
# Виконання завдань за допомогою Seaborn
# ======================================================================

print("=" * 80)
print("ЗАВДАННЯ 7")
print("Побудова графіків за допомогою Seaborn")

plt.figure(figsize=(12, 7))

sns.scatterplot(
    data=df,
    x='GDP_per_capita',
    y='Life_expectancy',
    hue='Category',
    size='Health_spending',
    sizes=(50, 500)
)

plt.title(
    "Seaborn: ВВП та тривалість життя",
    fontsize=18
)

plt.xlabel("ВВП на душу населення", fontsize=14)
plt.ylabel("Середня тривалість життя", fontsize=14)

plt.grid(True)

plt.show()

print("Seaborn графік побудовано")

# ======================================================================
# Plotly
# ======================================================================

print("=" * 80)
print("Plotly графік")

fig = px.bar(
    df,
    x='Country',
    y='GDP_per_capita',
    color='Country',
    title='Plotly: GDP per capita'
)

fig.show()

print("Plotly графік побудовано")

# ======================================================================
# КІНЕЦЬ РОБОТИ
# ======================================================================

print("=" * 80)
print("ПРАКТИЧНА РОБОТА УСПІШНО ЗАВЕРШЕНА")
print("=" * 80)