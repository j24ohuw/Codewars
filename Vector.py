import operator as op

class Vector:
  # TODO: Finish the Vector class.
  def __init__(self, array = []):
      self.__data = array
  
  def __iter__(self):
      return iter(self.__data)

  def check_length(func):
      def wrapper(self, other):
          if len(self.__data) != len(other.__data):
              raise ValueError()
          return func(self, other)
      return wrapper
  
  
  @check_length
  def add(self, other):
      return Vector(map(op.add, self, other))
  @check_length
  def subtract(self, other):
      return Vector(map(op.sub, self, other))
  @check_length
  def dot(self, other):
      return sum(Vector(map(op.mul, self, other)))

  def norm(self):
      return sum(Vector(map(lambda x: x**2, self)))**0.5
  
  def equals(self, other):
      return all(map(op.eq, self, other))
  
  def __str__(self):
      return '(%s)' %','.join(str(i) for i in self.__data)
      
