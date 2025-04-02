def fahrenheit_para_celsius(valor):
     #Calculo de transformação fahrenheit_para_celsius
     return (valor - 32) / 1.8


def celsius_para_fahrenheit(valor):
    #Calculo de transformação celsius_para_fahrenheit
    return (valor * 1.8) + 32 


def test():
    assert fahrenheit_para_celsius(104) == 40
    assert fahrenheit_para_celsius(-13) == -25

    assert celsius_para_fahrenheit(40) == 104
    assert celsius_para_fahrenheit(-25) == -13

    assert celsius_para_fahrenheit(fahrenheit_para_celsius(30)) == 30

print(celsius_para_fahrenheit(fahrenheit_para_celsius(30)) == 30)