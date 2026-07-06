class Vector:
    def __init__(self, values):
        self.values = values
        self.shape = (len(values), len(values[0]) if isinstance(values[0], list) else 1)

    def dot(self, other):
        """produces a dot product between two vectors of same shape"""
        if self.shape != other.shape:
            raise ValueError("Incompatible shapes for dot product")
        else:
            result = 0.0
            for i in range(self.shape[0]):
                for j in range(self.shape[1]):
                    result += self.values[i][j] * other.values[i][j]
            return result

    def T(self):
        """returns the transpose vector"""
        if self.shape[0] == 1:
            transpose = Vector([[self.values[0][i]] for i in range(self.shape[1])])
        else:
            transpose = Vector([[self.values[i][0] for i in range(self.shape[0])]])
        return transpose

    def __add__(self, other):
        """adds two vectors of same shape"""
        if self.shape != other.shape:
            raise ValueError("Incompatible shapes for addition")
        else:
            result = [[self.values[i][j] + other.values[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Vector(result)

    def __radd__(self, other):
        """Gère l'addition d'un vecteur par un scalaire (ex: 2.0 + v1)"""
        return self.__add__(other)

    def __sub__(self, other):
        """subtracts two vectors of same shape"""
        if self.shape != other.shape:
            raise ValueError("Incompatible shapes for subtraction")
        else:
            result = [[self.values[i][j] - other.values[i][j] for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Vector(result)
        
    def __rsub__(self, other):
        """Gère la soustraction d'un vecteur par un scalaire (ex: 2.0 - v1)"""
        return self.__sub__(other)

    def __mul__(self, scalar):
        """multiplies the vector by a scalar"""
        if not isinstance(scalar, (int, float)):
            raise ValueError("Multiplication is only defined for scalars")
        else:
            result = [[self.values[i][j] * scalar for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Vector(result)
        
    def __rmul__(self, scalar):
        """Gère la multiplication d'un scalaire par un vecteur (ex: 2.0 * v1)"""
        return self.__mul__(scalar)
    
    def __truediv__(self, scalar):
        """divides the vector by a scalar"""
        if not isinstance(scalar, (int, float)):
            raise ValueError("Division is only defined for scalars")
        if scalar == 0.0:
            raise ZeroDivisionError("division by zero.")
        else:
            result = [[self.values[i][j] / scalar for j in range(self.shape[1])] for i in range(self.shape[0])]
            return Vector(result)
        
    def __rtruediv__(self, scalar):
        """Gère la division d'un scalaire par un vecteur (ex: 2.0 / v1)"""
        raise NotImplementedError("Division of a scalar by a Vector is not defined here.")

    def __str__(self):
        """Définit ce qui s'affiche quand on utilise print()"""
        return str(self.values)

    def __repr__(self):
        """Définit ce qui s'affiche dans la console interactive ou avec repr()"""
        return f"Vector({self.values})"