import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('vmaf_summary.csv')

plt.figure(figsize=(10, 6))
plt.plot(df['Bitrate_kbps'], df['VMAF'], marker='o', linestyle='-', linewidth=2, markersize=8, color="#000000")

for i, row in df.iterrows():
    plt.annotate(row['Resolution'], (row['Bitrate_kbps'], row['VMAF']),
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.title('Rate-Distortion Curve (VMAF vs Bitrate)', fontsize=14, fontweight='bold')
plt.xlabel('Bitrate (kbps)', fontsize=12)
plt.ylabel('Average VMAF Score', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

plt.savefig('rd_curve.png', dpi=150, bbox_inches='tight')
