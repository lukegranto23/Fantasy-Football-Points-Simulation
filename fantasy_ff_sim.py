import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)
qbs = np.random.normal(loc=22, scale=6, size=10)
rbs = np.random.normal(loc=17, scale=8, size=10)
wrs = np.random.normal(loc=14, scale=7, size=10)

scores = np.concatenate([qbs, rbs, wrs])
positions = ['QB'] * 10 + ['RB'] * 10 + ['WR'] * 10

ff_df = pd.DataFrame({'Position': positions, 'Points': scores})
plt.figure(figsize=(10, 6))

# Create boxplot
ax = ff_df.boxplot(column='Points', by='Position', grid=False, patch_artist=True,
                   boxprops=dict(facecolor='lightblue'))

# Add individual data points as dots
positions = ['QB', 'RB', 'WR']
colors = ['red', 'green', 'blue']

for i, pos in enumerate(positions):
    pos_data = ff_df[ff_df['Position'] == pos]['Points']
    # Add some jitter to spread out the dots horizontally
    jitter = np.random.normal(i+1, 0.05, len(pos_data))
    plt.scatter(jitter, pos_data, alpha=0.6, s=50, color=colors[i], 
                label=f'{pos} Players')

plt.title('Fantasy Football: Weekly Point Distribution by Position')
plt.suptitle('')
plt.ylabel('Points per Game')
plt.xlabel('Player Position')
plt.legend()
plt.tight_layout()
plt.savefig('fantasy_ff_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()
