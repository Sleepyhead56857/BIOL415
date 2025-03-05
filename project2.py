import numpy as np
import matplotlib.pyplot as plt

# Define the file path (update this to your actual file path)
file_path = "fig2_c.txt"  # Change this to your actual file

# Load the data (modify delimiter if needed)
data = np.loadtxt(file_path, delimiter=None)  # Auto-detects space/tab separation

# Extract columns
x = data[:, 0]  # First column for X-axis
BT = data[:, 1]  # Second column for Y-axis
C_CA = data[:,2]

# Plot the data
plt.figure()
plt.plot(x, BT, linestyle='-', color='r', label=r"B_T(t)")
plt.plot(x, C_CA, linestyle = '--', color= 'r', linewidth = 1, label= r"C_CA125")
plt.axvline(x = 3677, linestyle = '--', color= 'r', linewidth = 1, label= r"D_T = 3677 days = 10.1 years")

# Labels and title
plt.xlabel("t (days)")
plt.ylabel("Conceration U/ml")
plt.title("Dynamics of CA-125 biomarker (Tumour + Healthy Cell Shedding)")
plt.ylim(0,140000)
plt.xlim(0,4000)
plt.legend(loc = 'best')
plt.grid(False)

# Show the plot
#plt.show()


# Define the file path (update this to your actual file path)
file_path = "fig2_b.txt"  # Change this to your actual file

# Load the data (modify delimiter if needed)
data = np.loadtxt(file_path, delimiter=None)  # Auto-detects space/tab separation

# Extract columns
x = data[:, 0]  # First column for X-axis
BT = data[:, 1]  # Second column for Y-axis
D_CA = data[:,2]

# Plot the data
plt.figure()
plt.plot(x, BT, linestyle='-', color='r', label=r"B_T(t)")
plt.plot(x, D_CA, linestyle = '--', color= 'r', linewidth = 1, label= r"C_CA125")
plt.axvline(x = 3221, linestyle = '--', color= 'r', linewidth = 1, label= r"D_T = 3221 days = 8.8 years")

# Labels and title
plt.xlabel("t (days)")
plt.ylabel("Conceration U/ml")
plt.title("Dynamics of CA-125 biomarker (Tumour + Healthy Cell Shedding)")
plt.ylim(0,100000)
plt.xlim(0,4000)
plt.legend(loc = 'best')
plt.grid(False)

# Show the plot
plt.show()