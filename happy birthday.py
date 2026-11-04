import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patheffects

plt.switch_backend("Agg")


def scatter_particles(ax, x, y, radius, count, color, size=12, alpha=0.9):
    """在圆盘中随机分布粒子"""
    ang = np.random.rand(count) * 2 * np.pi
    r = np.sqrt(np.random.rand(count)) * radius
    px = x + r * np.cos(ang)
    py = y + r * np.sin(ang)
    ax.scatter(px, py, s=size, c=color, alpha=alpha, edgecolors="none")


def scatter_ring(ax, cx, cy, r_inner, r_outer, count, color, size=12, alpha=0.9):
    """在环形区域随机生成粒子"""
    ang = np.random.rand(count) * 2 * np.pi
    r = np.sqrt(np.random.rand(count)) * (r_outer - r_inner) + r_inner
    px = cx + r * np.cos(ang)
    py = cy + r * np.sin(ang)
    ax.scatter(px, py, s=size, c=color, alpha=alpha, edgecolors="none")


def candle(ax, x, y, height=0.9):
    """绘制蜡烛"""
    # 烛身
    ax.plot([x, x], [y, y + height], color="#f9f1d6", lw=2.5, alpha=0.9)
    # 烛芯
    ax.scatter([x], [y + height], s=90, color="#f6d77a", alpha=0.95, edgecolors="none")
    # 火焰
    n = 120
    ang = np.random.rand(n) * 2 * np.pi
    rr = np.sqrt(np.random.rand(n)) * 0.24
    fx = x + rr * np.cos(ang)
    fy = y + height + 0.18 + rr * np.sin(ang) * 1.5
    ax.scatter(fx, fy, s=25, c="#ff8c42", alpha=0.85, edgecolors="none")


# 画布
fig, ax = plt.subplots(figsize=(8, 8), dpi=180)
bg = "#fffaf5"
fig.patch.set_facecolor(bg)
ax.set_facecolor(bg)
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.axis("off")

# 标题
title = ax.text(
    5, 8.8, "Happy birthday!",
    ha="center", va="center",
    fontsize=28, fontweight="bold",
    color="#ff5d8f",
    family="DejaVu Sans"
)
title.set_path_effects([
    patheffects.Stroke(linewidth=3, foreground="#ffffff"),
    patheffects.Normal()
])

# 蛋糕底座
scatter_particles(ax, 5, 1.8, 3.5, 2600, "#f4c7a1", size=10, alpha=0.92)
scatter_particles(ax, 5, 3.0, 2.9, 2200, "#f7d9a7", size=10, alpha=0.95)
scatter_particles(ax, 5, 4.0, 2.2, 1800, "#fbe7d2", size=10, alpha=0.96)

# 上层奶油
scatter_ring(ax, 5, 4.4, 1.6, 2.4, 900, "#fffdf9", size=12, alpha=0.95)

# 顶部的小糖珠装饰
colors = ["#ff6b6b", "#ffd166", "#06d6a0", "#4cc9f0", "#8ecae6", "#f72585", "#ff9f1c"]
for _ in range(220):
    ang = np.random.rand() * 2 * np.pi
    r = np.random.rand() * 2.1
    x = 5 + r * np.cos(ang)
    y = 4.2 + r * np.sin(ang) * 0.75
    ax.scatter([x], [y], s=18, c=np.random.choice(colors), alpha=0.9, edgecolors="none")

# 顶部装饰纹理
for _ in range(150):
    ang = np.random.uniform(-1.3, 1.3)
    rr = np.random.uniform(1.4, 2.3)
    x = 5 + rr * np.cos(ang)
    y = 4.6 + rr * np.sin(ang) * 0.55 + 0.3
    ax.scatter([x], [y], s=13, c="#ffffff", alpha=0.7, edgecolors="none")

# 蜡烛
for cx in [3.7, 4.5, 5.0, 5.5, 6.3]:
    candle(ax, cx, 4.7, height=1.0)

# 蛋糕底部阴影
scatter_particles(ax, 5, 0.6, 4.0, 500, "#e9c9b8", size=9, alpha=0.35)

plt.savefig("birthday_cake_particles_v2.png", dpi=200, bbox_inches="tight", facecolor=bg)
print("已生成：birthday_cake_particles_v2.png")