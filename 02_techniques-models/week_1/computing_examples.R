set.seed(42)

# Set priors and number of draws
m <- 100  # Increases accuracy with higher m
a <- 2.0
b <- 1.0 / 3.0

theta <- rgamma(m, shape=a, rate=b)

# Plot Theta
hist(theta, freq=FALSE)
curve(dgamma(x, shape=a, rate=b), col="blue", add=TRUE)

# Calculate Average 
theta_star <- sum(theta) / m  # note expected value is a / b = 6.0

m <- 10000
theta <- rgamma(m, shape=a, rate=b)
print(sum(theta) / m)  # This estimate is much closer

# Calculate variance of theta
var(theta)  # note var is a / b^2 = 18.0

# Calculate the probability of less than 5
inds <- theta < 5.0
mean(inds)  # Gives prob that we want above
print(pgamma(q=5.0, shape=a, rate=b))

# What about the 90th percentile?
quantile(theta, probs=0.9)
print(qgamma(p=0.9, shape=a, rate=b))  # Note how `q` and `p` switch places

# Note that for the posterior distributions, we won't have such nice functions to compare with.

