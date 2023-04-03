import numpy as np
import matplotlib.pyplot as plt

# Define the parameters of the sine wave
amplitude = 1
frequency = 5
phase = np.pi / 2

# Create an array of time values
t = np.arange(0, 2 * np.pi, 0.01)

# Calculate the sine wave values
sine_wave = amplitude * np.sin(frequency * t + phase)

# Add Gaussian noise to the sine wave
mean = 0
std_dev = 0.2
noise = np.random.normal(mean, std_dev, len(sine_wave))
noisy_wave = sine_wave + noise

# Plot the sine wave with noise
plt.plot(t, noisy_wave)
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.title('Sine Wave with Gaussian Noise')
plt.show()
