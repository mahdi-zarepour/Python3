"""

Open-Close Principle
این قانون میگه که شما باید جوری برنامه نویسی کنید که اگه برنامتون نیاز به گسترش داشت، ویژگی های جدید رو بتونید بدون تغییر دادن کدهای قبلی، به برنامه اضافه کنید

example about cart

"""
from abc import ABC, abstractmethod


# Abstract
class PriceRule(ABC):
    @abstractmethod
    def rule_type(self):
        pass

class Calculator(ABC):
    @abstractmethod
    def calculate(self):
        pass


# New Rule and Calculator
class PriceRuleFood(PriceRule):
    def rule_type(self, quantity, price):
        return CalculatorFood().calculate(quantity, price)

class CalculatorFood(Calculator):
    def calculate(self, quantity, price):
        return quantity * price


class PriceRuleLapTop(PriceRule):
    def rule_type(self, quantity, price):
        return CalculatorLapTop().calculate(quantity, price)

class CalculatorLapTop(Calculator):
    def calculate(self, quantity, price):
        if quantity >= 5:
           return (quantity - 1) * price
        else:
            return quantity * price


# Strategy
class Cart:
    def __call__(self, rule_type, quantity, price):
        return rule_type().rule_type(quantity, price)