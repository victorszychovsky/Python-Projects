import math # Przyda się za chwilę do koła!

def pobierz_liczbe(komunikat):
    """Funkcja pomocnicza, która wymusza na użytkowniku podanie poprawnej liczby."""
    while True:
        try:
            # Próbujemy pobrać i zamienić na float
            wartosc = float(input(komunikat))
            
            # Dodatkowe zabezpieczenie: figura nie może mieć boku na minusie!
            if wartosc <= 0:
                print("Błąd: Wartość musi być większa od zera! Spróbuj ponownie.")
                continue
                
            return wartosc # Zwracamy poprawną liczbę i wychodzimy z pętli
            
        except ValueError:
            # Ten blok wykona się tylko wtedy, gdy ktoś wpisze np. literę
            print("Błąd: To nie jest poprawna liczba. Spróbuj ponownie.")

# --- KLASA BAZOWA (RODZIC) ---
class Shape:
    def area(self):
        # NotImplementedError to profesjonalny sposób na powiedzenie:
        # "Każda figura MUSI mieć pole, ale każda liczy je inaczej. 
        # Zdefiniuj to we własnej klasie!"
        raise NotImplementedError("Podklasa musi zaimplementować metodę area()")

    def perimeter(self):
        raise NotImplementedError("Podklasa musi zaimplementować metodę perimeter()")


# --- KLASY POCHODNE (DZIECI) ---

# W nawiasie (Shape) mówimy Pythonowi: Kwadrat dziedziczy po Kształcie
class Square(Shape):
    def __init__(self, a):
        self.a = a
        
    def area(self):
        return self.a * self.a
        
    def perimeter(self): 
        return 4 * self.a

class Circle(Shape):
    def __init__(self, r): 
        self.r = r 
        self.pi = math.pi

    def area(self): 
        return self.pi * self.r * self.r 

    def perimeter(self): 
        return 2 * self.pi * self.r 


# Triangle
class Triangle(Shape):
    def __init__(self, a, b, c, h): 
        self.a = a
        self.b = b
        self.c = c
        self.h = h
    def area(self):
        return 0.5 * self.a * self.h
    def perimeter(self): 
        return self.a + self.b + self.c
triangle = Triangle(3, 4, 5, 2)

print("Pole trójkąta wynosi: ", triangle.area())
print("Obwód trójkąta wynosi: ", triangle.perimeter())

# --- INTERFEJS UŻYTKOWNIKA (Uruchomi się tylko bezpośrednio) ---
if __name__ == "__main__":
    print("=== WITAJ W KALKULATORZE FIGUR GEOMETRYCZNYCH ===")

    # --- KWADRAT ---
    print("\n--- KWADRAT ---")
    bok_kwadratu = pobierz_liczbe("Podaj długość boku kwadratu: ")
    square = Square(bok_kwadratu)
    print(f"Pole: {square.area()}")
    print(f"Obwód: {square.perimeter()}")

    # --- KOŁO ---
    print("\n--- KOŁO ---")
    promien = pobierz_liczbe("Podaj promień koła: ")
    circle = Circle(promien)
    print(f"Pole: {round(circle.area(), 2)}")
    print(f"Obwód: {round(circle.perimeter(), 2)}")

    # --- TRÓJKĄT ---
    print("\n--- TRÓJKĄT ---")
    print("Podaj wymiary trójkąta:")
    bok_a = pobierz_liczbe("Bok a (podstawa): ")
    bok_b = pobierz_liczbe("Bok b: ")
    bok_c = pobierz_liczbe("Bok c: ")
    wysokosc = pobierz_liczbe("Wysokość h (opuszczona na bok a): ")

    triangle = Triangle(bok_a, bok_b, bok_c, wysokosc)
    print(f"Pole: {triangle.area()}")
    print(f"Obwód: {triangle.perimeter()}")