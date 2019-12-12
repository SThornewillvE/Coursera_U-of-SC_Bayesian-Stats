set.seed(42)

m <- 10000
a <- 2.0
b <- 1.0 / 3.0

theta <- rgamma(n=m, shape=a, rate=b)

se = sd(theta) / sqrt(m)
print(se)  # We could use this to compute a confidence interval

# Calculate confident interval
print(mean(theta) - 2*se)
print(mean(theta) + 2*se)

# What's the probability that the value is less than 5
ind = theta < 5
mean(ind)
pgamma(5.0, shape=a, rate=b)

se = sd(ind) / sqrt(m)

# Let's try to simulate from a heirarchical model
m = 1e5
y = numeric(m)
phi = numeric(m)

for (i in 1:m) {  # R is slow in loops
  phi[i] = rbeta(1, shape1=2.0, shape2=2.0)
  y[i] = rbinom(1, size=10, prob=phi[i])
}

# Can we write the above using vectorised code?
phi = rbeta(m, shape1=2.0, shape2=2.0)
y = rbinom(m, size=10, prob=phi)

# How many times did we get each success?
table(y) / m

# Got plots?
plot(table(y)/m)

# What is the mean of y?
mean(y)
