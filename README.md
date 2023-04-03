This Python script simulates a sine wave with added Gaussian noise using the NumPy and Matplotlib libraries.

Installation

To run this script, you'll need to have the following Python packages installed:

NumPy
Matplotlib
You can install these packages using pip:

pip install numpy matplotlib
Usage

To use this script, simply run it in a Python environment:

python sine.py
This will generate a plot of a sine wave with added Gaussian noise, with the parameters defined in the script.

Customization

You can customize the parameters of the sine wave and Gaussian noise by editing the following lines in the script:

python
amplitude = 1
frequency = 5
phase = np.pi / 2
mean = 0
std_dev = 0.2
amplitude: The amplitude of the sine wave.
frequency: The frequency of the sine wave in hertz.
phase: The phase of the sine wave in radians.
mean: The mean of the Gaussian noise.
std_dev: The standard deviation of the Gaussian noise.
You can also customize the time range and step size by editing the following line:

python
Copy code
t = np.arange(0, 2 * np.pi, 0.01)
The first argument is the start time.
The second argument is the end time.
The third argument is the time step size.
License

This script is released under the MIT License. See the LICENSE file for details.
