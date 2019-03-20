def es_primo(n):
    div=2
    vof=True
    while (vof is True) and (div <= n):
        mod = n % div
        if (mod == 0) and (div != n):
            vof = False
        div += 1
    return vof


assert es_primo(2)
assert es_primo(6) is False

