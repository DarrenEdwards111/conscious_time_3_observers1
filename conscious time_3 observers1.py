import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def observer_trajectory(t_values, branch_id):
    # Initialize trajectories as arrays
    x_traj = np.sin(t_values) * 2 + branch_id * 0.5  # Base oscillatory motion with initial spatial offset
    y_traj = np.cos(t_values) * 2 + branch_id * 0.5
    tau_traj = t_values * 0.5 + branch_id * 1.0  # Base τ offset (increased for clearer separation)
    
    # Introduce branching: after t=5, there is a chance to diverge further
    current_branch = branch_id
    for i, t in enumerate(t_values):
        if t > 5 and np.random.random() < 0.5:  # 50% chance of branching after t=5
            # Increase branch level (simulate divergence)
            current_branch += 1
            # Apply a jump offset to subsequent values to show branching
            x_traj[i:] += 1.0
            y_traj[i:] += 1.0
            tau_traj[i:] += 1.0
            # Break after branching once to avoid too many splits in a single trajectory
            break
    return x_traj, y_traj, tau_traj

# Generate time range for the trajectories
t_range = np.linspace(0, 10, 50)

# Create a 3D plot for observer trajectories with branching
fig2 = plt.figure(figsize=(10, 8))
ax2 = fig2.add_subplot(111, projection='3d')

# Plot trajectories for three initial branches
for branch in range(3):
    x_traj, y_traj, tau_traj = observer_trajectory(t_range, branch)
    ax2.plot(x_traj, y_traj, tau_traj, label=f'Observer Branch {branch + 1}', linewidth=2)

ax2.set_xlabel('X (Spatial)')
ax2.set_ylabel('Y (Spatial)')
ax2.set_zlabel('Conscious Observer Time (τ)')
ax2.set_title('Example Observer Trajectories with Pronounced Branching in the 5D Manifold')
ax2.legend()
plt.show()
