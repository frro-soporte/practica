def es_primo(m):
    if m <= 1:
        return True
    
    limit = int(m ** 0.5 + 1)

    return not any(m % i == 0 for i in range(2, limit))

# Case for 1
assert es_primo(1) is True

# Case for prime number
assert es_primo(17) is True

# Case for non-prime number
assert es_primo(18) is False