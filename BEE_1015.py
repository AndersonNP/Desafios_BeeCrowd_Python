valorX1, valorY1 = map(float, input().split())
valorX2, valorY2 = map(float, input().split())

distancia = ((valorX2 - valorX1)**2 + (valorY2 - valorY1)**2)**0.5
print(f"{distancia:.4f}")
