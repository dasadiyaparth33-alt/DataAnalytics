import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

cricket_stats = {
    'cricketer' : ['Sachin Tendulkar','MS Dhoni','Virat Kohli','Suresh Raina','Ravindra Jadeja','Rohit Sharma'],
    'fifties' : [68, 73, 43, 18, 12, 50],
    'hundreds' : [100, 10, 27, 1, 1, 39],
}
df_cricket = pd.DataFrame(cricket_stats)
print(df_cricket)

# print("="*50)
# df_cricket.style.set_properties(subset=['cricketer'],**{'text-align':'left'})
# print("="*50)
# print(df_cricket)

print("="*50)
# unpivot the data frame
df_log = df_cricket.melt(id_vars="cricketer", var_name="Score Type", value_name="Count")
print(df_log)

#Visualization
# Render grouped bar plot via seaborn
plt.figure(figsize=(10,6))
sns.barplot(x="cricketer", y="Count", hue="Score Type", data=df_log)
plt.legend(loc='upper right')
plt.xticks(rotation=45, ha='right')
plt.title("International Cricketer Performance: Fifties and Hundreds")
plt.xlabel("Cricketer")
plt.ylabel("Score Count")
plt.tight_layout()
plt.show()