import h5py
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
import scienceplots
from tqdm import tqdm
from icecream import ic


plt.style.use(["science"])
plt.rcParams["font.size"] = "10.5"
plt.rc("text", usetex=True)


with h5py.File("data/u_om_kx_kz0.h5", "r") as f: # keep your data in one directory
    ic(f.keys()) # Check available datasets and names
    u_real = f["uRealPart"][:]
    u_imag = f["uImaginaryPart"][:]
    kx = f["kx"][:]
    omega = f["omega"][:]

x = np.linspace(0, 4*np.pi, u_real.shape[2])  # Assuming x is normalized
y = np.linspace(-1, 1, u_real.shape[1])


u_hat = u_real + 1j * u_imag # u_hat are the Fourier coefficients (directly relate to your sine wave parameters)
u_w = np.fft.ifft(u_hat, axis=0)
window = np.hanning(u_w.shape[0])
window[window == 0] = 1
u = u_w / window[:, np.newaxis, np.newaxis]
u = np.fft.ifft(u, axis=2)

fig, ax = plt.subplots(1, 1, figsize=(5, 6), sharex=True, sharey=True, tight_layout=True)
ax.contourf(x, y, np.abs(u[15, :, :]), levels=100, cmap=sns.color_palette("crest", as_cmap=True))
ax.set_xlabel(r"$x$")
ax.set_ylabel(r"$y$")
fig.savefig("figures/u_k0.png", dpi=700)
