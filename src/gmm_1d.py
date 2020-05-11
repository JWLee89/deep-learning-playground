"""
@Author Jay Lee
A simple 1d Gaussian mixture model
for fitting 1d datasets
"""
import math

class GMM:
    def __init__(self, mus, sigmas, mixture_prob):
        self.mus = mus
        self.sigmas = sigmas
        self.pi = mixture_prob

    def fit(self, X, iterations=2):
        for i in range(iterations):
            self.update(X)

    def _gaussian1d(self, x, i):
        return self.pi[i] / self.sigmas[i] / (2 * math.pi) ** (1 / 2) * math.exp(-(x - self.mus[i]) ** 2 / (2 * self.sigmas[i] ** 2))

    def responsibility(self, x, i):
        target = self._gaussian1d(x, i)
        total = 0
        for k in range(len(self.mus)):
            if k != i:
                total += self._gaussian1d(x, j)
        total += target
        return target / total

    def update(self, X):
        new_mu = []
        new_sigma = []
        new_pi = []
        for k in range(len(self.mus)):
            total = 0
            total_res = 0
            std_dev = 0
            for i, data in enumerate(X):
                responsibility = self.responsibility(data, k)
                total += data * responsibility
                total_res += responsibility
                std_dev += (responsibility * ((data - self.mus[k]) ** 2))

            # Calculate parameters
            mu = total / total_res
            sigma = (std_dev / total_res) ** (1 / 2)
            pi = total_res / len(X)
            # Add parameters to list
            new_mu.append(mu)
            new_sigma.append(sigma)
            new_pi.append(pi)

        # update params
        self.mus = new_mu
        self.pi = new_pi
        self.sigmas = new_sigma
        

if __name__ == "__main__":
    X = [1, 2, 4, 7, 8, 10]
    mu = [1, 10]
    sigma = [1, 1]
    pi = [0.5, 0.5]
    em = GMM(mu, sigma, pi)
    em.fit(X, iterations=2)
    print("Final results: ")
    print("Means: ", em.mus)
    print("Pi: ", em.pi)
    print("Sigma: ", em.sigmas)
