import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")
sns.set_theme(style="ticks", color_codes=True)

# sns.catplot(x="sex",y="survived", hue="class", kind="bar",data=titanic)
# plt.show()


# p1 = sns.countplot(x='sex',data=titanic, hue='class')
# p1.set_title("Plot for Counting")
# plt.show()

g= sns.FacetGrid(titanic, row='sex', hue='alone')
g=(g.map(plt.scatter,'age', 'fare').add_legend())
plt.show()